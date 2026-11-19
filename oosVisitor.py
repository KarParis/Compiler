# Generated from oos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .oosParser import oosParser
else:
    from oosParser import oosParser

# This class defines a complete generic visitor for a parse tree produced by oosParser.

class oosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by oosParser#startRule.
    def visitStartRule(self, ctx:oosParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#classes.
    def visitClasses(self, ctx:oosParser.ClassesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#class_def.
    def visitClass_def(self, ctx:oosParser.Class_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#class_main_def.
    def visitClass_main_def(self, ctx:oosParser.Class_main_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#class_name.
    def visitClass_name(self, ctx:oosParser.Class_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#declarations.
    def visitDeclarations(self, ctx:oosParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#class_body.
    def visitClass_body(self, ctx:oosParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#main_body.
    def visitMain_body(self, ctx:oosParser.Main_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#decl_line.
    def visitDecl_line(self, ctx:oosParser.Decl_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#constructor_def.
    def visitConstructor_def(self, ctx:oosParser.Constructor_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#method_def.
    def visitMethod_def(self, ctx:oosParser.Method_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#method_main_def.
    def visitMethod_main_def(self, ctx:oosParser.Method_main_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#types.
    def visitTypes(self, ctx:oosParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#parameters.
    def visitParameters(self, ctx:oosParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#method_body.
    def visitMethod_body(self, ctx:oosParser.Method_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#return_type.
    def visitReturn_type(self, ctx:oosParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#parlist.
    def visitParlist(self, ctx:oosParser.ParlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#statements.
    def visitStatements(self, ctx:oosParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#statement.
    def visitStatement(self, ctx:oosParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#assignment_stat.
    def visitAssignment_stat(self, ctx:oosParser.Assignment_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#direct_call_stat.
    def visitDirect_call_stat(self, ctx:oosParser.Direct_call_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#if_stat.
    def visitIf_stat(self, ctx:oosParser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#else_part.
    def visitElse_part(self, ctx:oosParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#while_stat.
    def visitWhile_stat(self, ctx:oosParser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#return_stat.
    def visitReturn_stat(self, ctx:oosParser.Return_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#input_stat.
    def visitInput_stat(self, ctx:oosParser.Input_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#print_stat.
    def visitPrint_stat(self, ctx:oosParser.Print_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#expression.
    def visitExpression(self, ctx:oosParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#arguments.
    def visitArguments(self, ctx:oosParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#condition.
    def visitCondition(self, ctx:oosParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#optional_sign.
    def visitOptional_sign(self, ctx:oosParser.Optional_signContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#term.
    def visitTerm(self, ctx:oosParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#add_oper.
    def visitAdd_oper(self, ctx:oosParser.Add_operContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#arglist.
    def visitArglist(self, ctx:oosParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#boolterm.
    def visitBoolterm(self, ctx:oosParser.BooltermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#factor.
    def visitFactor(self, ctx:oosParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#mul_oper.
    def visitMul_oper(self, ctx:oosParser.Mul_operContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#argitem.
    def visitArgitem(self, ctx:oosParser.ArgitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#boolfactor.
    def visitBoolfactor(self, ctx:oosParser.BoolfactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#func_call.
    def visitFunc_call(self, ctx:oosParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#constructor_call.
    def visitConstructor_call(self, ctx:oosParser.Constructor_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by oosParser#rel_oper.
    def visitRel_oper(self, ctx:oosParser.Rel_operContext):
        return self.visitChildren(ctx)



del oosParser