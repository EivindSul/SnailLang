import sys
from antlr4 import *
from .parser.SnailParser import SnailParser
from .parser.SnailVisitor import SnailVisitor
from .symbols import SymbolTable

def snailPrint(*args):
    print(*args)

class Interpreter(SnailVisitor):

    def __init__(self, sym:SymbolTable) -> None:
        sym.define_builtin("print", print)
        self.sym = sym

    def visitProgram(self, ctx: SnailParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitForeach(self, ctx: SnailParser.ForeachContext):
        # | FOR_KEYWORD EACH_KEYWORD each_range IN_KEYWORD atom block # foreach
        return super().visitForeach(ctx)

    def visitEach_range(self, ctx: SnailParser.Each_rangeContext):
        # each_range
        # 	: ID (COMMA ID)?
        # 	;
        ids = ctx.ID()
        match len(ids):
            case 1:
                print("1 id")
            case 2:
                print("2 id")
            case _:
                print("invalid!")

        print("For each is not supported yet. Terminating...")
        sys.exit(1)

    def visitWhile(self, ctx: SnailParser.WhileContext):
        while True:
            if not self.visit(ctx.expr()):
                break
            self.visit(ctx.block())

    def visitRange(self, ctx: SnailParser.RangeContext):
        range_ = {}
        range_["loop_var"] = ctx.ID().getText()
        range_["start"] = 0
        range_["end"] = 0
        range_["step_size"] = 1

        # HACK: visit does not work, just extract the text instead.
        # ints = [self.visit(i) for i in ctx.INT()]
        ints = [int(i.getText()) for i in ctx.INT()]

        match len(ints):
            case 2:
                range_["start"] = ints[0]
                range_["end"] = ints[1]
            case 3:
                range_["start"] = ints[0]
                range_["end"] = ints[1]
                range_["step_size"] = ints[2]
            case _:
                raise SyntaxError(f"Expected 2 or 3 ints in for-range statement. Received {len(ints)}.")

        return range_

    def visitForrange(self, ctx: SnailParser.ForrangeContext):

        range_ = self.visit(ctx.range_())

        loop_var = range_["loop_var"]
        start = range_["start"]
        end = range_["end"]
        step_size = range_["step_size"]

        for i in range(start, end, step_size):
            loop_context = SymbolTable(parent=self.sym)
            loop_context.set_local(loop_var, i)
            interpreter = Interpreter(loop_context)
            interpreter.visit(ctx.block())

    def visitIf(self, ctx: SnailParser.IfContext):
        if self.visit(ctx.ifstat()):
            return
        for i in ctx.elifstat():
            if self.visit(i.ifstat()):
                return
        if ctx.elsestat():
            self.visit(ctx.elsestat().block())

    def visitIfstat(self, ctx: SnailParser.IfstatContext):
        if self.visit(ctx.expr()):
            self.visit(ctx.block())
            return True
        else:
            return False

    def visitBlock(self, ctx: SnailParser.BlockContext):
        interpreter = Interpreter(SymbolTable(parent=self.sym))
        interpreter.visitChildren(ctx)

    def visitExpr(self, ctx: SnailParser.ExprContext):
        return self.visitChildren(ctx)

    def visitGlobalassign(self, ctx:SnailParser.GlobalassignContext):
        id = ctx.ID().getText()
        expr = ctx.expr()
        self.sym.set_global(id, self.visit(expr))

    def visitLocalassign(self, ctx:SnailParser.LocalassignContext):
        id = ctx.ID().getText()
        expr = ctx.expr()
        value = self.visit(expr)
        self.sym.set_local(id, value)

    def visitAdd(self, ctx:SnailParser.AddContext):
        return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(2))

    def visitSub(self, ctx:SnailParser.SubContext):
        return self.visit(ctx.getChild(0)) - self.visit(ctx.getChild(2))

    def visitMul(self, ctx:SnailParser.MulContext):
        return self.visit(ctx.getChild(0)) * self.visit(ctx.getChild(2))

    def visitDiv(self, ctx:SnailParser.DivContext):
        return self.visit(ctx.getChild(0)) // self.visit(ctx.getChild(2))

    def visitLessthan(self, ctx:SnailParser.LessthanContext):
        return self.visit(ctx.getChild(0)) < self.visit(ctx.getChild(2))

    def visitLessorequal(self, ctx:SnailParser.LessorequalContext):
        return self.visit(ctx.getChild(0)) <= self.visit(ctx.getChild(2))

    def visitGreaterthan(self, ctx:SnailParser.GreaterthanContext):
        return self.visit(ctx.getChild(0)) > self.visit(ctx.getChild(2))

    def visitGreaterorequal(self, ctx:SnailParser.GreaterorequalContext):
        return self.visit(ctx.getChild(0)) >= self.visit(ctx.getChild(2))

    def visitNotequal(self, ctx:SnailParser.NotequalContext):
        return self.visit(ctx.getChild(0)) != self.visit(ctx.getChild(2))

    def visitEqual(self, ctx:SnailParser.EqualContext):
        return self.visit(ctx.getChild(0)) == self.visit(ctx.getChild(2))

    def visitNot(self, ctx:SnailParser.NotContext):
        return not self.visit(ctx.getChild(1))

    def visitAnd(self, ctx:SnailParser.AndContext):
        return self.visit(ctx.getChild(0)) and self.visit(ctx.getChild(2))

    def visitOr(self, ctx:SnailParser.OrContext):
        return self.visit(ctx.getChild(0)) or self.visit(ctx.getChild(2))

    def visitConcat(self, ctx:SnailParser.ConcatContext):
        return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(2))

    def visitNested(self, ctx:SnailParser.NestedContext):
        return self.visit(ctx.expr())

    def visitIntliteral(self, ctx:SnailParser.IntliteralContext):
        return int(ctx.getText())

    def visitFloatliteral(self, ctx:SnailParser.FloatliteralContext):
        return float(ctx.getText())

    def visitStringliteral(self, ctx:SnailParser.StringliteralContext):
        return str(ctx.getText())[1:-1] # Remove quotes

    def visitBoolliteral(self, ctx:SnailParser.BoolliteralContext):
        return ctx.getText() == "true"

    def visitNullliteral(self, ctx:SnailParser.NullliteralContext):
        return None

    def visitIdentifier(self, ctx:SnailParser.IdentifierContext):
        content = None

        try:
            content = self.sym.get(ctx.getText())
        except NameError:
            pass

        return content

    def visitCall(self, ctx:SnailParser.CallContext):
        func = self.sym.get(ctx.ID().getText())
        args = self.visit(ctx.arg_list())
        func(*args)

    def visitArg_list(self, ctx:SnailParser.Arg_listContext):
        return [ self.visit(i) for i in ctx.expr() ]
