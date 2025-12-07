# Generated from grammar/RachaConta.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,3,0,24,8,0,1,0,5,0,27,8,
        0,10,0,12,0,30,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,4,2,41,8,
        2,11,2,12,2,42,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,3,4,56,
        8,4,1,5,1,5,1,5,5,5,61,8,5,10,5,12,5,64,9,5,1,6,1,6,1,6,1,6,1,6,
        3,6,71,8,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,
        8,10,12,14,16,18,20,0,0,75,0,23,1,0,0,0,2,34,1,0,0,0,4,38,1,0,0,
        0,6,44,1,0,0,0,8,55,1,0,0,0,10,57,1,0,0,0,12,65,1,0,0,0,14,72,1,
        0,0,0,16,74,1,0,0,0,18,76,1,0,0,0,20,78,1,0,0,0,22,24,3,2,1,0,23,
        22,1,0,0,0,23,24,1,0,0,0,24,28,1,0,0,0,25,27,3,4,2,0,26,25,1,0,0,
        0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,31,1,0,0,0,30,28,
        1,0,0,0,31,32,5,1,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,35,5,2,0,0,35,
        36,5,12,0,0,36,37,5,15,0,0,37,3,1,0,0,0,38,40,3,6,3,0,39,41,5,15,
        0,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,5,
        1,0,0,0,44,45,5,3,0,0,45,46,3,16,8,0,46,47,5,4,0,0,47,48,3,20,10,
        0,48,49,5,5,0,0,49,50,3,14,7,0,50,51,5,6,0,0,51,52,3,8,4,0,52,7,
        1,0,0,0,53,56,5,7,0,0,54,56,3,10,5,0,55,53,1,0,0,0,55,54,1,0,0,0,
        56,9,1,0,0,0,57,62,3,12,6,0,58,59,5,8,0,0,59,61,3,12,6,0,60,58,1,
        0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,11,1,0,0,0,64,
        62,1,0,0,0,65,70,5,11,0,0,66,67,5,9,0,0,67,68,3,18,9,0,68,69,5,10,
        0,0,69,71,1,0,0,0,70,66,1,0,0,0,70,71,1,0,0,0,71,13,1,0,0,0,72,73,
        5,11,0,0,73,15,1,0,0,0,74,75,5,14,0,0,75,17,1,0,0,0,76,77,5,13,0,
        0,77,19,1,0,0,0,78,79,5,12,0,0,79,21,1,0,0,0,6,23,28,42,55,62,70
    ]

class RachaContaParser ( Parser ):

    grammarFileName = "RachaConta.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'fechar'", "'evento'", "'gasto'", "'em'", 
                     "'por'", "'para'", "'todos'", "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "STRING", 
                      "INT", "NUMBER", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_title = 1
    RULE_statement = 2
    RULE_expense = 3
    RULE_beneficiaries = 4
    RULE_list_of_people = 5
    RULE_person_share = 6
    RULE_payer = 7
    RULE_value = 8
    RULE_weight = 9
    RULE_description = 10

    ruleNames =  [ "program", "title", "statement", "expense", "beneficiaries", 
                   "list_of_people", "person_share", "payer", "value", "weight", 
                   "description" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ID=11
    STRING=12
    INT=13
    NUMBER=14
    NEWLINE=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RachaContaParser.EOF, 0)

        def title(self):
            return self.getTypedRuleContext(RachaContaParser.TitleContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RachaContaParser.StatementContext)
            else:
                return self.getTypedRuleContext(RachaContaParser.StatementContext,i)


        def getRuleIndex(self):
            return RachaContaParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RachaContaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 22
                self.title()


            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 25
                self.statement()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.match(RachaContaParser.T__0)
            self.state = 32
            self.match(RachaContaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(RachaContaParser.STRING, 0)

        def NEWLINE(self):
            return self.getToken(RachaContaParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RachaContaParser.RULE_title

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTitle" ):
                return visitor.visitTitle(self)
            else:
                return visitor.visitChildren(self)




    def title(self):

        localctx = RachaContaParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(RachaContaParser.T__1)
            self.state = 35
            self.match(RachaContaParser.STRING)
            self.state = 36
            self.match(RachaContaParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expense(self):
            return self.getTypedRuleContext(RachaContaParser.ExpenseContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(RachaContaParser.NEWLINE)
            else:
                return self.getToken(RachaContaParser.NEWLINE, i)

        def getRuleIndex(self):
            return RachaContaParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = RachaContaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.expense()
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.match(RachaContaParser.NEWLINE)
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpenseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(RachaContaParser.ValueContext,0)


        def description(self):
            return self.getTypedRuleContext(RachaContaParser.DescriptionContext,0)


        def payer(self):
            return self.getTypedRuleContext(RachaContaParser.PayerContext,0)


        def beneficiaries(self):
            return self.getTypedRuleContext(RachaContaParser.BeneficiariesContext,0)


        def getRuleIndex(self):
            return RachaContaParser.RULE_expense

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpense" ):
                return visitor.visitExpense(self)
            else:
                return visitor.visitChildren(self)




    def expense(self):

        localctx = RachaContaParser.ExpenseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expense)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(RachaContaParser.T__2)
            self.state = 45
            self.value()
            self.state = 46
            self.match(RachaContaParser.T__3)
            self.state = 47
            self.description()
            self.state = 48
            self.match(RachaContaParser.T__4)
            self.state = 49
            self.payer()
            self.state = 50
            self.match(RachaContaParser.T__5)
            self.state = 51
            self.beneficiaries()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BeneficiariesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_of_people(self):
            return self.getTypedRuleContext(RachaContaParser.List_of_peopleContext,0)


        def getRuleIndex(self):
            return RachaContaParser.RULE_beneficiaries

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBeneficiaries" ):
                return visitor.visitBeneficiaries(self)
            else:
                return visitor.visitChildren(self)




    def beneficiaries(self):

        localctx = RachaContaParser.BeneficiariesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_beneficiaries)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(RachaContaParser.T__6)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.list_of_people()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_peopleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def person_share(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RachaContaParser.Person_shareContext)
            else:
                return self.getTypedRuleContext(RachaContaParser.Person_shareContext,i)


        def getRuleIndex(self):
            return RachaContaParser.RULE_list_of_people

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_people" ):
                return visitor.visitList_of_people(self)
            else:
                return visitor.visitChildren(self)




    def list_of_people(self):

        localctx = RachaContaParser.List_of_peopleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list_of_people)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.person_share()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 58
                self.match(RachaContaParser.T__7)
                self.state = 59
                self.person_share()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Person_shareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RachaContaParser.ID, 0)

        def weight(self):
            return self.getTypedRuleContext(RachaContaParser.WeightContext,0)


        def getRuleIndex(self):
            return RachaContaParser.RULE_person_share

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPerson_share" ):
                return visitor.visitPerson_share(self)
            else:
                return visitor.visitChildren(self)




    def person_share(self):

        localctx = RachaContaParser.Person_shareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_person_share)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(RachaContaParser.ID)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 66
                self.match(RachaContaParser.T__8)
                self.state = 67
                self.weight()
                self.state = 68
                self.match(RachaContaParser.T__9)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PayerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RachaContaParser.ID, 0)

        def getRuleIndex(self):
            return RachaContaParser.RULE_payer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayer" ):
                return visitor.visitPayer(self)
            else:
                return visitor.visitChildren(self)




    def payer(self):

        localctx = RachaContaParser.PayerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_payer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(RachaContaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(RachaContaParser.NUMBER, 0)

        def getRuleIndex(self):
            return RachaContaParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = RachaContaParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(RachaContaParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RachaContaParser.INT, 0)

        def getRuleIndex(self):
            return RachaContaParser.RULE_weight

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeight" ):
                return visitor.visitWeight(self)
            else:
                return visitor.visitChildren(self)




    def weight(self):

        localctx = RachaContaParser.WeightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_weight)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(RachaContaParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(RachaContaParser.STRING, 0)

        def getRuleIndex(self):
            return RachaContaParser.RULE_description

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescription" ):
                return visitor.visitDescription(self)
            else:
                return visitor.visitChildren(self)




    def description(self):

        localctx = RachaContaParser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(RachaContaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





