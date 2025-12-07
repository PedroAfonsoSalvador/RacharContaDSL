# Generated from grammar/RachaConta.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RachaContaParser import RachaContaParser
else:
    from RachaContaParser import RachaContaParser

# This class defines a complete generic visitor for a parse tree produced by RachaContaParser.

class RachaContaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RachaContaParser#program.
    def visitProgram(self, ctx:RachaContaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RachaContaParser#title.
    def visitTitle(self, ctx:RachaContaParser.TitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RachaContaParser#statement.
    def visitStatement(self, ctx:RachaContaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RachaContaParser#expense.
    def visitExpense(self, ctx:RachaContaParser.ExpenseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RachaContaParser#beneficiaries.
    def visitBeneficiaries(self, ctx:RachaContaParser.BeneficiariesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RachaContaParser#list_of_people.
    def visitList_of_people(self, ctx:RachaContaParser.List_of_peopleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RachaContaParser#person_share.
    def visitPerson_share(self, ctx:RachaContaParser.Person_shareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RachaContaParser#payer.
    def visitPayer(self, ctx:RachaContaParser.PayerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RachaContaParser#value.
    def visitValue(self, ctx:RachaContaParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RachaContaParser#weight.
    def visitWeight(self, ctx:RachaContaParser.WeightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RachaContaParser#description.
    def visitDescription(self, ctx:RachaContaParser.DescriptionContext):
        return self.visitChildren(ctx)



del RachaContaParser