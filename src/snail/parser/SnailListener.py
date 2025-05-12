# Generated from Snail.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SnailParser import SnailParser
else:
    from SnailParser import SnailParser

# This class defines a complete listener for a parse tree produced by SnailParser.
class SnailListener(ParseTreeListener):

    # Enter a parse tree produced by SnailParser#program.
    def enterProgram(self, ctx:SnailParser.ProgramContext):
        pass

    # Exit a parse tree produced by SnailParser#program.
    def exitProgram(self, ctx:SnailParser.ProgramContext):
        pass


    # Enter a parse tree produced by SnailParser#assignment.
    def enterAssignment(self, ctx:SnailParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SnailParser#assignment.
    def exitAssignment(self, ctx:SnailParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SnailParser#forrange.
    def enterForrange(self, ctx:SnailParser.ForrangeContext):
        pass

    # Exit a parse tree produced by SnailParser#forrange.
    def exitForrange(self, ctx:SnailParser.ForrangeContext):
        pass


    # Enter a parse tree produced by SnailParser#foreach.
    def enterForeach(self, ctx:SnailParser.ForeachContext):
        pass

    # Exit a parse tree produced by SnailParser#foreach.
    def exitForeach(self, ctx:SnailParser.ForeachContext):
        pass


    # Enter a parse tree produced by SnailParser#while.
    def enterWhile(self, ctx:SnailParser.WhileContext):
        pass

    # Exit a parse tree produced by SnailParser#while.
    def exitWhile(self, ctx:SnailParser.WhileContext):
        pass


    # Enter a parse tree produced by SnailParser#conditional.
    def enterConditional(self, ctx:SnailParser.ConditionalContext):
        pass

    # Exit a parse tree produced by SnailParser#conditional.
    def exitConditional(self, ctx:SnailParser.ConditionalContext):
        pass


    # Enter a parse tree produced by SnailParser#patmat.
    def enterPatmat(self, ctx:SnailParser.PatmatContext):
        pass

    # Exit a parse tree produced by SnailParser#patmat.
    def exitPatmat(self, ctx:SnailParser.PatmatContext):
        pass


    # Enter a parse tree produced by SnailParser#return.
    def enterReturn(self, ctx:SnailParser.ReturnContext):
        pass

    # Exit a parse tree produced by SnailParser#return.
    def exitReturn(self, ctx:SnailParser.ReturnContext):
        pass


    # Enter a parse tree produced by SnailParser#expression.
    def enterExpression(self, ctx:SnailParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SnailParser#expression.
    def exitExpression(self, ctx:SnailParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SnailParser#patternmatch.
    def enterPatternmatch(self, ctx:SnailParser.PatternmatchContext):
        pass

    # Exit a parse tree produced by SnailParser#patternmatch.
    def exitPatternmatch(self, ctx:SnailParser.PatternmatchContext):
        pass


    # Enter a parse tree produced by SnailParser#patterneval.
    def enterPatterneval(self, ctx:SnailParser.PatternevalContext):
        pass

    # Exit a parse tree produced by SnailParser#patterneval.
    def exitPatterneval(self, ctx:SnailParser.PatternevalContext):
        pass


    # Enter a parse tree produced by SnailParser#pattern.
    def enterPattern(self, ctx:SnailParser.PatternContext):
        pass

    # Exit a parse tree produced by SnailParser#pattern.
    def exitPattern(self, ctx:SnailParser.PatternContext):
        pass


    # Enter a parse tree produced by SnailParser#if.
    def enterIf(self, ctx:SnailParser.IfContext):
        pass

    # Exit a parse tree produced by SnailParser#if.
    def exitIf(self, ctx:SnailParser.IfContext):
        pass


    # Enter a parse tree produced by SnailParser#elif.
    def enterElif(self, ctx:SnailParser.ElifContext):
        pass

    # Exit a parse tree produced by SnailParser#elif.
    def exitElif(self, ctx:SnailParser.ElifContext):
        pass


    # Enter a parse tree produced by SnailParser#else.
    def enterElse(self, ctx:SnailParser.ElseContext):
        pass

    # Exit a parse tree produced by SnailParser#else.
    def exitElse(self, ctx:SnailParser.ElseContext):
        pass


    # Enter a parse tree produced by SnailParser#block.
    def enterBlock(self, ctx:SnailParser.BlockContext):
        pass

    # Exit a parse tree produced by SnailParser#block.
    def exitBlock(self, ctx:SnailParser.BlockContext):
        pass


    # Enter a parse tree produced by SnailParser#range.
    def enterRange(self, ctx:SnailParser.RangeContext):
        pass

    # Exit a parse tree produced by SnailParser#range.
    def exitRange(self, ctx:SnailParser.RangeContext):
        pass


    # Enter a parse tree produced by SnailParser#each_range.
    def enterEach_range(self, ctx:SnailParser.Each_rangeContext):
        pass

    # Exit a parse tree produced by SnailParser#each_range.
    def exitEach_range(self, ctx:SnailParser.Each_rangeContext):
        pass


    # Enter a parse tree produced by SnailParser#namedkey.
    def enterNamedkey(self, ctx:SnailParser.NamedkeyContext):
        pass

    # Exit a parse tree produced by SnailParser#namedkey.
    def exitNamedkey(self, ctx:SnailParser.NamedkeyContext):
        pass


    # Enter a parse tree produced by SnailParser#exprkey.
    def enterExprkey(self, ctx:SnailParser.ExprkeyContext):
        pass

    # Exit a parse tree produced by SnailParser#exprkey.
    def exitExprkey(self, ctx:SnailParser.ExprkeyContext):
        pass


    # Enter a parse tree produced by SnailParser#listitem.
    def enterListitem(self, ctx:SnailParser.ListitemContext):
        pass

    # Exit a parse tree produced by SnailParser#listitem.
    def exitListitem(self, ctx:SnailParser.ListitemContext):
        pass


    # Enter a parse tree produced by SnailParser#add.
    def enterAdd(self, ctx:SnailParser.AddContext):
        pass

    # Exit a parse tree produced by SnailParser#add.
    def exitAdd(self, ctx:SnailParser.AddContext):
        pass


    # Enter a parse tree produced by SnailParser#sub.
    def enterSub(self, ctx:SnailParser.SubContext):
        pass

    # Exit a parse tree produced by SnailParser#sub.
    def exitSub(self, ctx:SnailParser.SubContext):
        pass


    # Enter a parse tree produced by SnailParser#lessorequal.
    def enterLessorequal(self, ctx:SnailParser.LessorequalContext):
        pass

    # Exit a parse tree produced by SnailParser#lessorequal.
    def exitLessorequal(self, ctx:SnailParser.LessorequalContext):
        pass


    # Enter a parse tree produced by SnailParser#or.
    def enterOr(self, ctx:SnailParser.OrContext):
        pass

    # Exit a parse tree produced by SnailParser#or.
    def exitOr(self, ctx:SnailParser.OrContext):
        pass


    # Enter a parse tree produced by SnailParser#mul.
    def enterMul(self, ctx:SnailParser.MulContext):
        pass

    # Exit a parse tree produced by SnailParser#mul.
    def exitMul(self, ctx:SnailParser.MulContext):
        pass


    # Enter a parse tree produced by SnailParser#lessthan.
    def enterLessthan(self, ctx:SnailParser.LessthanContext):
        pass

    # Exit a parse tree produced by SnailParser#lessthan.
    def exitLessthan(self, ctx:SnailParser.LessthanContext):
        pass


    # Enter a parse tree produced by SnailParser#greaterthan.
    def enterGreaterthan(self, ctx:SnailParser.GreaterthanContext):
        pass

    # Exit a parse tree produced by SnailParser#greaterthan.
    def exitGreaterthan(self, ctx:SnailParser.GreaterthanContext):
        pass


    # Enter a parse tree produced by SnailParser#notequal.
    def enterNotequal(self, ctx:SnailParser.NotequalContext):
        pass

    # Exit a parse tree produced by SnailParser#notequal.
    def exitNotequal(self, ctx:SnailParser.NotequalContext):
        pass


    # Enter a parse tree produced by SnailParser#concat.
    def enterConcat(self, ctx:SnailParser.ConcatContext):
        pass

    # Exit a parse tree produced by SnailParser#concat.
    def exitConcat(self, ctx:SnailParser.ConcatContext):
        pass


    # Enter a parse tree produced by SnailParser#div.
    def enterDiv(self, ctx:SnailParser.DivContext):
        pass

    # Exit a parse tree produced by SnailParser#div.
    def exitDiv(self, ctx:SnailParser.DivContext):
        pass


    # Enter a parse tree produced by SnailParser#equal.
    def enterEqual(self, ctx:SnailParser.EqualContext):
        pass

    # Exit a parse tree produced by SnailParser#equal.
    def exitEqual(self, ctx:SnailParser.EqualContext):
        pass


    # Enter a parse tree produced by SnailParser#not.
    def enterNot(self, ctx:SnailParser.NotContext):
        pass

    # Exit a parse tree produced by SnailParser#not.
    def exitNot(self, ctx:SnailParser.NotContext):
        pass


    # Enter a parse tree produced by SnailParser#and.
    def enterAnd(self, ctx:SnailParser.AndContext):
        pass

    # Exit a parse tree produced by SnailParser#and.
    def exitAnd(self, ctx:SnailParser.AndContext):
        pass


    # Enter a parse tree produced by SnailParser#functiondeclaration.
    def enterFunctiondeclaration(self, ctx:SnailParser.FunctiondeclarationContext):
        pass

    # Exit a parse tree produced by SnailParser#functiondeclaration.
    def exitFunctiondeclaration(self, ctx:SnailParser.FunctiondeclarationContext):
        pass


    # Enter a parse tree produced by SnailParser#atomic.
    def enterAtomic(self, ctx:SnailParser.AtomicContext):
        pass

    # Exit a parse tree produced by SnailParser#atomic.
    def exitAtomic(self, ctx:SnailParser.AtomicContext):
        pass


    # Enter a parse tree produced by SnailParser#greaterorequal.
    def enterGreaterorequal(self, ctx:SnailParser.GreaterorequalContext):
        pass

    # Exit a parse tree produced by SnailParser#greaterorequal.
    def exitGreaterorequal(self, ctx:SnailParser.GreaterorequalContext):
        pass


    # Enter a parse tree produced by SnailParser#table.
    def enterTable(self, ctx:SnailParser.TableContext):
        pass

    # Exit a parse tree produced by SnailParser#table.
    def exitTable(self, ctx:SnailParser.TableContext):
        pass


    # Enter a parse tree produced by SnailParser#tablelookup.
    def enterTablelookup(self, ctx:SnailParser.TablelookupContext):
        pass

    # Exit a parse tree produced by SnailParser#tablelookup.
    def exitTablelookup(self, ctx:SnailParser.TablelookupContext):
        pass


    # Enter a parse tree produced by SnailParser#call.
    def enterCall(self, ctx:SnailParser.CallContext):
        pass

    # Exit a parse tree produced by SnailParser#call.
    def exitCall(self, ctx:SnailParser.CallContext):
        pass


    # Enter a parse tree produced by SnailParser#nested.
    def enterNested(self, ctx:SnailParser.NestedContext):
        pass

    # Exit a parse tree produced by SnailParser#nested.
    def exitNested(self, ctx:SnailParser.NestedContext):
        pass


    # Enter a parse tree produced by SnailParser#intliteral.
    def enterIntliteral(self, ctx:SnailParser.IntliteralContext):
        pass

    # Exit a parse tree produced by SnailParser#intliteral.
    def exitIntliteral(self, ctx:SnailParser.IntliteralContext):
        pass


    # Enter a parse tree produced by SnailParser#floatliteral.
    def enterFloatliteral(self, ctx:SnailParser.FloatliteralContext):
        pass

    # Exit a parse tree produced by SnailParser#floatliteral.
    def exitFloatliteral(self, ctx:SnailParser.FloatliteralContext):
        pass


    # Enter a parse tree produced by SnailParser#stringliteral.
    def enterStringliteral(self, ctx:SnailParser.StringliteralContext):
        pass

    # Exit a parse tree produced by SnailParser#stringliteral.
    def exitStringliteral(self, ctx:SnailParser.StringliteralContext):
        pass


    # Enter a parse tree produced by SnailParser#boolliteral.
    def enterBoolliteral(self, ctx:SnailParser.BoolliteralContext):
        pass

    # Exit a parse tree produced by SnailParser#boolliteral.
    def exitBoolliteral(self, ctx:SnailParser.BoolliteralContext):
        pass


    # Enter a parse tree produced by SnailParser#nullliteral.
    def enterNullliteral(self, ctx:SnailParser.NullliteralContext):
        pass

    # Exit a parse tree produced by SnailParser#nullliteral.
    def exitNullliteral(self, ctx:SnailParser.NullliteralContext):
        pass


    # Enter a parse tree produced by SnailParser#identifier.
    def enterIdentifier(self, ctx:SnailParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SnailParser#identifier.
    def exitIdentifier(self, ctx:SnailParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SnailParser#arg_list.
    def enterArg_list(self, ctx:SnailParser.Arg_listContext):
        pass

    # Exit a parse tree produced by SnailParser#arg_list.
    def exitArg_list(self, ctx:SnailParser.Arg_listContext):
        pass


    # Enter a parse tree produced by SnailParser#param_list.
    def enterParam_list(self, ctx:SnailParser.Param_listContext):
        pass

    # Exit a parse tree produced by SnailParser#param_list.
    def exitParam_list(self, ctx:SnailParser.Param_listContext):
        pass


    # Enter a parse tree produced by SnailParser#param.
    def enterParam(self, ctx:SnailParser.ParamContext):
        pass

    # Exit a parse tree produced by SnailParser#param.
    def exitParam(self, ctx:SnailParser.ParamContext):
        pass


    # Enter a parse tree produced by SnailParser#sep.
    def enterSep(self, ctx:SnailParser.SepContext):
        pass

    # Exit a parse tree produced by SnailParser#sep.
    def exitSep(self, ctx:SnailParser.SepContext):
        pass



del SnailParser