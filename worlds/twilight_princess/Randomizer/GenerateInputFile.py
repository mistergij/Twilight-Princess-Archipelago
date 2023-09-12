import os
import random
import sys


class GenerateInputFile:
    def __init__(self):
        self.__charMap = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
        
    def __genID(self):
        num = 0
        charIndex = 0
        id_string = ''
        
        for i in range(0,2):
            num = random.randint(0, 0xFFFFFFFF)
            for j in range(0, 5):
                charIndex = num & (0x3F)
                id_string += self.__charMap[charIndex]
                num >>= 6
            
            num = random.randint(0, 0xFFFFFFFF)
            charIndex = num & (0x3F)
            id_string += self.__charMap[charIndex]
            
            return id_string
        
        def Run(self, settingsString):
            success = False
            id_string = self.__genID()
            outputPath = os.path.join("seeds", id_string, "input.json")
            
            try:
                os.makedir(os.path.dirname(outputPath))
                f = open(outputPath, "w")
                f.write(settingsString)
                f.close()

                print("SUCCESS:" + id_string)
                success = True
            except:
                print("Problem writing input.json file for id: " + id_string)
                sys.exit(1)
                
            return success
                