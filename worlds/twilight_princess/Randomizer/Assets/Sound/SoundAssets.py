import json
import os
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from Logic.FcSettingsEnums import RandomizeBgm


class SoundAssets:
    
    def __init__(self):
        self.IncompatibleReplacements = (
            (62, 148)
            (62, 98)
            (44, 8)
            (55, 8)
        )
        self.incompatible = False
    
    class _bgmReplacement:
        def __init__(self):
            self.originalBgmTrack = 0
            self.replacementBgmTrack = 0
            self.replacementBgmWave = 0
    
    class _bgmData:
        def __init__(self):
            self.name = ""
            self.internalName = ""
            self.bgmId = 0
            self.bgmWave = 0
            self.sceneBgm = False
            self.dungeonBgm = False
            self.minibossBgm = False
            self.bossBgm = False
            self.minigameBgm = False
            self.cutsceneBgm = False
            self.isFanfare = False
    
    def GenerateBgmData(self, seedData):
        data = []
        replacementPool = []
        bgmReplacementArray = []
        if seedData.fcSettings.randomizeBgm == RandomizeBgm.Off.value:
            return data
        with open(os.path.join(Path(__file__).parent, 'BackgroundMusic.json')) as json_file:
            dataList = json.load(json_file)
            
        if seedData.fcsettings.randomizeBgm != RandomizeBgm.Off.value:
            for currentData in dataList.items():
                
                if seedData.fcSettings.randomizeBgm == RandomizeBgm.Overworld.value and currentData[1]["sceneBgm"] == True:
                    replacementPool.append(currentData[1])
                    
                if seedData.fcSettings.randomizeBgm == RandomizeBgm.Dungeon.value and currentData[1]["dungeonBgm"] == True:
                    replacementPool.append(currentData[1])
                
                if seedData.fcSettings.randomizeBgm == RandomizeBgm.All.value and (currentData[1]["sceneBgm"] == True or currentData[1]["dungeonBgm"] == True or currentData[1]["minigameBgm"] == True or currentData[1]["eventBgm"] == True):
                    replacementPool.append(currentData[1])

            for currentData in replacementPool:
                replacement = self._bgmReplacement
                replacement.replacementBgmTrack = currentData["bgmID"]
                replacement.replacementBgmWave = currentData["bgmWave"]
                
                while True:
                    replacement.originalBgmTrack = replacementPool[random.randint(0, len(replacementPool)-1)]["bgmID"]
                    foundSame = False
                    for currentReplacement in bgmReplacementArray:
                        if currentReplacement.originalBgmTrack == replacement.originalBgmTrack:
                            foundSame = True
                            break
                    
                    if foundSame == False:
                        self.incompatible = False
                        for i in range(0, len(self.IncompatibleReplacements)):
                            original = self.IncompatibleReplacements[i][0]
                            replacementBgm = self.IncompatibleReplacements[i][1]
                            if original == replacement.originalBgmTrack:
                                if replacementBgm == replacement.replacementBgmTrack:
                                    self.incompatible = True
                                
                        if not self.incompatible:
                            break
                    
                bgmReplacementArray.append(replacement)
                
            if len(replacementPool) != len(bgmReplacementArray):
                print(f"BGM Pool ({len(replacementPool)}) and Replacement ({len(bgmReplacementArray)}) have different lengths!")
            
            for currentReplacement in bgmReplacementArray:
                data.append(currentReplacement.originalBgmTrack.value)
                data.append(currentReplacement.replacementBgmTrack.value)
                data.append(currentReplacement.replacementBgmWave.value)
                data.append(0x0)
            
        seedData.BgmHeaderRaw.bgmTableNumEntries = len(bgmReplacementArray)
        seedData.BgmHeaderRaw.bgmTableSize = len(data)
        return data