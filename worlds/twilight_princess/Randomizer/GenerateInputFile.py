import os
import random
import sys

class GenerateInputFile:
    def __init__(self):
        self._charMap = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    
    def _genId(self):
        num = 0
        charIndex = 0
        id_string = ""
        
        for i in range(0, 5):
            num = random.randint(0, 2147483647)
            for j in range(0, 5):
                charIndex = num & (0x3F)
                id_string += self._charMap[charIndex]
                num = num >> 6
        
        num = random.randint(0, 2147483647)
        charIndex &= (0X3F)
        id_string += self._charMap[charIndex]
        
        return id_string
    
    def Run(self, settingsString):
        def __init__(self):
            self.success = False
            self.id = self.genId()
            self.outputPath = os.path.join("seeds", id, "input.json")
        
        try:
            os.mkdir(os.path.dirname(self.outputPath))
            f = open(self.outputPath, 'w')
            f.write(settingsString)
            f.close()
            
            print(f"SUCCESS: {self.id}")
            self.success = True
        except:
            print(f"Problem writing input.json file for id: {self.id}")
            sys.exit(1)
        
        return self.success