import sys
from antlr4 import *
from .parser.SnailParser import SnailParser
from .parser.SnailVisitor import SnailVisitor
from .symbols import SymbolTable

from llvmlite import ir
import llvmlite.binding as llvm

INT_TYPE = ir.IntType(32)
STR_TYPE = ir.IntType(32)
FLT_TYPE = ir.IntType(32)
TRUE = ir.Constant(ir.IntType(1), 1)
FALSE = ir.Constant(ir.IntType(1), 0)

class Compiler(SnailVisitor):

    def __init__(self, sym:SymbolTable) -> None:
        self.sym = sym

        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        module = ir.Module(name="snail")
        target = llvm.Target.from_default_triple()
        machine = target.create_target_machine()
        module.triple = machine.triple
        module.data_layout = str(machine.target_data)
        self.module = module

        printtype = ir.FunctionType(INT_TYPE, (ir.PointerType(),))
        printf = ir.Function(self.module, printtype, name="printf")
        self.sym.define_builtin("print", printf)

        functype = ir.FunctionType(INT_TYPE, (INT_TYPE, ir.PointerType()))
        mainfunc = ir.Function(self.module, functype, "main")
        mainbody = mainfunc.append_basic_block("entry")

        self.builder = ir.IRBuilder(mainbody)


    def visitProgram(self, ctx: SnailParser.ProgramContext):
        self.visitChildren(ctx)
        self.builder.ret(ir.Constant(INT_TYPE, 0))
        return self.module

    def visitGlobalassign(self, ctx:SnailParser.GlobalassignContext):
        id = ctx.ID().getText()
        expr = ctx.expr()
        value = self.visit(expr)
        expr_type = value.type

        try:
            ptr = self.sym.get(id)
            if expr_type == self.builder.load(ptr).type:
                self.builder.store(value, ptr)
            else:
                ptr = self.builder.alloca(expr_type, name=id)

        except NameError:
            ptr = self.builder.alloca(expr_type, name=id)

        self.builder.store(value, ptr)
        self.sym.assign(id, ptr)

    def visitLocalassign(self, ctx:SnailParser.LocalassignContext):
        id = ctx.ID().getText()
        expr = ctx.expr()
        value = self.visit(expr)
        expr_type = value.type

        try:
            ptr = self.sym.get(id)
            if expr_type == self.builder.load(ptr).type:
                self.builder.store(value, ptr)
            else:
                ptr = self.builder.alloca(expr_type, name=id)

        except NameError:
            ptr = self.builder.alloca(expr_type, name=id)

        self.builder.store(value, ptr)
        self.sym.set_local(id, ptr)

    def visitCall(self, ctx:SnailParser.CallContext):

        func = self.sym.get(ctx.ID().getText())

        args = self.visit(ctx.arg_list())

        #NOTE: Functions only take one argument. The rest are ignored.
        array_val = args[0]
        array_type = array_val.type

        ptr = self.builder.alloca(array_type)
        self.builder.store(array_val, ptr)

        self.builder.call(func, (ptr,))

    def visitArg_list(self, ctx:SnailParser.Arg_listContext):
        return [ self.visit(i) for i in ctx.expr() ]

    def visitIf(self, ctx: SnailParser.IfContext):

        func = self.builder.function

        cases = []

        for i, stat in enumerate(ctx.elifstat()):
            case = {}
            case["cond_block"] = func.append_basic_block(f"cond_{i}")
            case["then_block"] = func.append_basic_block(f"then_{i}")
            case["expr"] = stat.ifstat().expr()
            case["block"] = stat.ifstat().block()
            cases.append(case)

        if_block = func.append_basic_block("if")
        end_block = func.append_basic_block("end")
        else_block = end_block

        cond = self.visit(ctx.ifstat().expr())

        if cases:
            next_block = cases[0]["cond_block"]
        else:
            next_block = else_block

        self.builder.cbranch(cond, if_block, next_block)
        self.builder.position_at_start(if_block)
        self.visit(ctx.ifstat().block())
        self.builder.branch(end_block)

        if ctx.elsestat():
            else_block = func.append_basic_block("else")
            self.builder.position_at_start(else_block)
            self.visit(ctx.elsestat().block())
            self.builder.branch(end_block)

        for i, case in enumerate(cases):
            self.builder.position_at_start(case["cond_block"])

            cond = self.visit(case["expr"])

            if i + 1 < len(cases):
                self.builder.cbranch(cond, case["then_block"], cases[i + 1]["cond_block"])
            else:
                self.builder.cbranch(cond, case["then_block"], else_block)

            self.builder.position_at_start(case["then_block"])
            self.visit(case["block"])
            self.builder.branch(end_block)

        self.builder.position_at_start(end_block)

    def visitBlock(self, ctx: SnailParser.BlockContext):
        self.sym = SymbolTable(parent=self.sym)
        self.visitChildren(ctx)
        if not self.sym.parent:
            raise ValueError("A block is trying to exit, but the symbol table has no parent. How?")
        else:
            self.sym = self.sym.parent

    #NOTE: Only works for ints as of now :)
    def visitAdd(self, ctx:SnailParser.AddContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.add(lhs, rhs)

    def visitSub(self, ctx:SnailParser.SubContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.sub(lhs, rhs)

    def visitMul(self, ctx:SnailParser.MulContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.mul(lhs, rhs)

    def visitDiv(self, ctx:SnailParser.DivContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.sdiv(lhs, rhs)

    def visitLessthan(self, ctx:SnailParser.LessthanContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.icmp_signed("<", lhs, rhs)

    def visitLessorequal(self, ctx:SnailParser.LessorequalContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.icmp_signed("<=", lhs, rhs)

    def visitGreaterthan(self, ctx:SnailParser.GreaterthanContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.icmp_signed(">", lhs, rhs)

    def visitGreaterorequal(self, ctx:SnailParser.GreaterorequalContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.icmp_signed(">=", lhs, rhs)

    def visitNotequal(self, ctx:SnailParser.NotequalContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.icmp_signed("!=", lhs, rhs)

    def visitEqual(self, ctx:SnailParser.EqualContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.icmp_signed("==", lhs, rhs)

    def visitNot(self, ctx:SnailParser.NotContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.not_(lhs, rhs)

    def visitAnd(self, ctx:SnailParser.AndContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.and_(lhs, rhs)

    def visitOr(self, ctx:SnailParser.OrContext):
        lhs = self.visit(ctx.getChild(0))
        rhs = self.visit(ctx.getChild(2))
        return self.builder.or_(lhs, rhs)

    def visitConcat(self, ctx:SnailParser.ConcatContext):
        return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(2))

    def visitNested(self, ctx:SnailParser.NestedContext):
        #TODO: Prolly something
        return self.visit(ctx.expr())

    def visitIntliteral(self, ctx:SnailParser.IntliteralContext):
        return ir.Constant(INT_TYPE, int(ctx.getText()))

    def visitFloatliteral(self, ctx:SnailParser.FloatliteralContext):
        return ir.Constant(FLT_TYPE, int(ctx.getText()))
        # return float(ctx.getText())

    def visitStringliteral(self, ctx:SnailParser.StringliteralContext):
        string = str(ctx.getText())[1:-1] + "\n\0"
        stringb = string.encode()
        array_type = ir.ArrayType(ir.IntType(8), len(stringb))
        array_val = ir.Constant(array_type, bytearray(stringb))
        return array_val

    def visitBoolliteral(self, ctx:SnailParser.BoolliteralContext):
        if ctx.getText() == "true":
            return TRUE
        return FALSE

    def visitNullliteral(self, ctx:SnailParser.NullliteralContext):
        return ir.Undefined

    def visitIdentifier(self, ctx:SnailParser.IdentifierContext):
        value = None

        try:
            ptr = self.sym.get(ctx.getText())
            value = self.builder.load(ptr)
        except NameError:
            pass

        return value
