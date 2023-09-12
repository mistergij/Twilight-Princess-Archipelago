from abc import ABC, abstractmethod

from Randomizer.Randomizer import Randomizer as rando

  
class Token(ABC):
    pass

class OperandToken(Token):
    pass

class OrToken(OperandToken):
    pass

class AndToken(OperandToken):
    pass

class BooleanValueToken(Token):
    pass

class logicFunctionToken(Token):
    pass

class IntegerToken(Token):
    pass

class itemToken(Token):
    pass

class FalseToken(BooleanValueToken):
    pass

class TrueToken(BooleanValueToken):
    pass

class ParenthesisToken(Token):
    pass

class EqualsToken(Token):
    pass

class settingsToken(OperandToken):
    pass

class roomToken(OperandToken):
    pass

class CommaToken(Token):
    pass

class canUseToken(Token):
    pass

class ClosedParenthesisToken(ParenthesisToken):
    pass

class OpenParenthesisToken(ParenthesisToken):
    pass

class NegationToken(Token):
    pass
    
class NegationToken(Token):
    pass

class Parser:

    def __init__(self):
        self.tokenValue = 0
        self.isinParenthesis = 0
        self.checkedLogicItem = ""
        
    def ParserReset(self):
        self.tokenValue = 0
        rando.Logic.TokenDict.clear()
        
    def Parse(self):
        while(
            (list(rando.Logic.TokenDict.keys())[self.tokenValue] != None) and
            (not (self.tokenValue > (len(rando.Logic.TokenDict) - 1)))
        ):
            pass
        
    def __ParseBoolean(self):
        parseBool = False
        if (list(rando.Logic.TokenDict.keys())[self.tokenValue] is BooleanValueToken):
            current = list(rando.Logic.TokenDict.keys())[self.tokenValue]
            self.tokenValue += 1
            
            if (current is TrueToken):
                return True
            
            return False
        elif (list(rando.Logic.TokenDict.keys())[self.tokenValue] is OpenParenthesisToken):
            self.isinParenthesis += 1
            self.tokenValue += 1
            
            expinPars = self.Parse()
            if(
                not(
                    list(rando.Logic.TokenDict.keys())[self.tokenValue] is ClosedParenthesisToken
                )
            ):
                for i in range(self.tokenValue,len(rando.Logic.TokenDict)):
                    print(f"Stack Trace: {list(rando.Logic.TokenDict.values())[i]}")
                raise Exception(f"Expecting Closing Parenthesis but got: {list(rando.Logic.TokenDict.keys())[self.tokenValue]}")
            
            self.tokenValue += 1
            self.isinParenthesis -= 1
            
            return expinPars
        elif (list(rando.Logic.TokenDict.keys())[self.tokenValue] is ClosedParenthesisToken
              and (self.isinParenthesis == 0)):
            raise Exception(f"Unexpected Closed Parenthesis in location: {self.checkedLogicItem}")
        elif (list(rando.Logic.TokenDict.keys())[self.tokenValue] is itemToken):
            evaluatedItem = list(rando.Logic.TokenDict.values())[self.tokenValue]
            self.tokenValue += 1
            if (list(rando.Logic.TokenDict.keys())[self.tokenValue] is CommaToken):
                self.tokenValue += 1
                #TODO: Create LogicFunctions verifyItemQuantity method