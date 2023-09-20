import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from Logic.CheckIds import CheckIdClass
from Assets.CLR0.clr0Types import Clr0Entry


class SettingsEncoder:
    def __init__(self):
        self._charMap = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    
    def EncodeByteAs6BitChar(self, value):
        if value >= 64:
            raise Exception(f"Can't encode \"{value}\" to 6 bits.")
        
        return self._charMap[value]
    
    def EncodeAs6BitString(self, bitString):
        if (bitString == None) or (len(bitString) == 0):
            return ""
        
        result = ""
        
        remainder = len(bitString) % 6
        if (remainder > 0):
            loopCount = 6 - remainder
            for i in range(0, loopCount):
                bitString += "0"

        iterations = len(bitString) / 6
        for i in range(0, iterations):
            index = bitString[(i*6):((i*6)+6)]
            result += self._charMap[int(index, 2)]
        
        return result
    
    def DecodeToBitString(self, encodedStr):
        bitStr = ""
        
        for i in range(0, len(encodedStr)):
            bitStr += f"{self._charMap.find(encodedStr[i]):06b}"
        
        return bitStr
    
    def DecodeToInt(self, encodedStr):
        return int(self.DecodeToBitString(encodedStr), 2)
    
    def EncodeAsVlq16(self, num):
        if num < 65537:
            return f"{num:16b}"
        
    def DecodeVlq16(self, bits):
        return int(bits, 2)

    def EncodeNumAsBits(self, number, bitLength):
        return bin(number)[2:].zfill(bitLength)
    
class BitsProcessor:
    def __init__(self, bitString):
        self.bits = ""
        self.currentIndex = 0
        self.done = False
        if bitString != None and bitString != "":
            self.bits = bitString
        if len(self.bits) < 0:
            self.done = True
        
    def NextString(self, arr, bitLength = 4):
        if (self.done) or (len(self.bits) < (self.currentIndex + bitLength)):
            raise Exception("Not enough bits remaining")
        
        result = arr[int(self.bits[self.currentIndex:self.currentIndex + bitLength+1], 2)]
        
        self.currentIndex += bitLength
        
        if self.currentIndex >= len(self.bits):
            self.done = True
        
        return result
    
    def NextInt(self, numBits):
        if (self.done) or (len(self.bits) < (self.currentIndex + numBits)):
            raise Exception("Not enough bits remaining")
        
        result = int(self.bits[self.currentIndex:numBits+1], 2)
        
        self.currentIndex += numBits
        
        if self.currentIndex >= len(self.bits):
            self.done = True
        
        return result
    
    def NextUInt16(self):
        length = 16
        if (self.done) or (len(self.bits) < (self.currentIndex + length)):
            raise Exception("Not enough bits remaining")
        
        result = int(self.bits[self.currentIndex:self.currentIndex+length+1], 2)
        
        self.currentIndex += length
        
        if self.currentIndex >= len(self.bits):
            self.done = True
        
        return result
    
    def NextBool(self):
        length = 1
        if (self.done) or (len(self.bits) < (self.currentIndex + length)):
            raise Exception("Not enough bits remaining")
        
        result = self.bits[self.currentIndex] == "1"
        
        self.currentIndex += length
        
        if self.currentIndex >= len(self.bits):
            self.done = True
        
        return result
    
    def NextByte(self):
        length = 8
        if (self.done) or (len(self.bits) < (self.currentIndex + length)):
            raise Exception("Not enough bits remaining")
        
        result = self.bits[self.currentIndex:self.currentIndex+length+1]
        
        self.currentIndex += length
        
        if self.currentIndex >= len(self.bits):
            self.done = True
        
        return result
    
    def NextItemList(self):
        itemList = []
        
        while True:
            itemId = self.NextInt(9)
            if (itemId >= 0) and (itemId < 0x1FF):
                itemList.append(itemId)
            else:
                break
            
        return itemList
    
    def NextExcludedChecksList(self):
        excludedChecksList = []
        
        while True:
            checkIdNum = self.NextInt(9)
            if (checkIdNum >= 0) and (checkIdNum < 0x1FF):
                excludedChecksList.append(CheckIdClass.GetCheckName(checkIdNum))
            else:
                break
            
        return excludedChecksList
    
    def NextVlq16(self):
        if (self.done) or len(self.bits < (self.current_Index + 16)):
            raise Exception("Not enough bits remaining.")
        
        val = SettingsEncoder.DecodeVlq16(self.bits[self.currentIndex, self.currentIndex + 17])
        
        currentIndex += 16
        
        if self.currentIndex >= len(self.bits):
            done = True
            
        return val
    
    def NextClr0Entry(self, recolorId):
        
        pass