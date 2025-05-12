# Generated from Snail.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SnailParser import SnailParser
else:
    from SnailParser import SnailParser

# This class defines a complete generic visitor for a parse tree produced by SnailParser.

class SnailVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SnailParser#program.
    def visitProgram(self, ctx:SnailParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#assignment.
    def visitAssignment(self, ctx:SnailParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#forrange.
    def visitForrange(self, ctx:SnailParser.ForrangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#foreach.
    def visitForeach(self, ctx:SnailParser.ForeachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#while.
    def visitWhile(self, ctx:SnailParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#conditional.
    def visitConditional(self, ctx:SnailParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#patmat.
    def visitPatmat(self, ctx:SnailParser.PatmatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#return.
    def visitReturn(self, ctx:SnailParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#expression.
    def visitExpression(self, ctx:SnailParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#patternmatch.
    def visitPatternmatch(self, ctx:SnailParser.PatternmatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#patterneval.
    def visitPatterneval(self, ctx:SnailParser.PatternevalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#pattern.
    def visitPattern(self, ctx:SnailParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#if.
    def visitIf(self, ctx:SnailParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#elif.
    def visitElif(self, ctx:SnailParser.ElifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#else.
    def visitElse(self, ctx:SnailParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#block.
    def visitBlock(self, ctx:SnailParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#range.
    def visitRange(self, ctx:SnailParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#each_range.
    def visitEach_range(self, ctx:SnailParser.Each_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#namedkey.
    def visitNamedkey(self, ctx:SnailParser.NamedkeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#exprkey.
    def visitExprkey(self, ctx:SnailParser.ExprkeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#listitem.
    def visitListitem(self, ctx:SnailParser.ListitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#add.
    def visitAdd(self, ctx:SnailParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#sub.
    def visitSub(self, ctx:SnailParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#lessorequal.
    def visitLessorequal(self, ctx:SnailParser.LessorequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#or.
    def visitOr(self, ctx:SnailParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#mul.
    def visitMul(self, ctx:SnailParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#lessthan.
    def visitLessthan(self, ctx:SnailParser.LessthanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#greaterthan.
    def visitGreaterthan(self, ctx:SnailParser.GreaterthanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#notequal.
    def visitNotequal(self, ctx:SnailParser.NotequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#concat.
    def visitConcat(self, ctx:SnailParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#div.
    def visitDiv(self, ctx:SnailParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#equal.
    def visitEqual(self, ctx:SnailParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#not.
    def visitNot(self, ctx:SnailParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#and.
    def visitAnd(self, ctx:SnailParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#functiondeclaration.
    def visitFunctiondeclaration(self, ctx:SnailParser.FunctiondeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#atomic.
    def visitAtomic(self, ctx:SnailParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#greaterorequal.
    def visitGreaterorequal(self, ctx:SnailParser.GreaterorequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#table.
    def visitTable(self, ctx:SnailParser.TableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#tablelookup.
    def visitTablelookup(self, ctx:SnailParser.TablelookupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#call.
    def visitCall(self, ctx:SnailParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#nested.
    def visitNested(self, ctx:SnailParser.NestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#intliteral.
    def visitIntliteral(self, ctx:SnailParser.IntliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#floatliteral.
    def visitFloatliteral(self, ctx:SnailParser.FloatliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#stringliteral.
    def visitStringliteral(self, ctx:SnailParser.StringliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#boolliteral.
    def visitBoolliteral(self, ctx:SnailParser.BoolliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#nullliteral.
    def visitNullliteral(self, ctx:SnailParser.NullliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#identifier.
    def visitIdentifier(self, ctx:SnailParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#arg_list.
    def visitArg_list(self, ctx:SnailParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#param_list.
    def visitParam_list(self, ctx:SnailParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#param.
    def visitParam(self, ctx:SnailParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SnailParser#sep.
    def visitSep(self, ctx:SnailParser.SepContext):
        return self.visitChildren(ctx)



del SnailParser