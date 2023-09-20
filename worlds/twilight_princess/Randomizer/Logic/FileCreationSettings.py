import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from Util.SettingsEncoder import BitsProcessor
from FcSettingsEnums import GameRegion, RandomizeBgm


class FileCreationSettings:
    def __init__(self):
        self.gameRegion = None
        self.includeSpoilerLog = True
        self.randomizeBgm = None
        self.randomizeFanfares = False
        self.disableEnemyBgm = False
        
        self.hTunicHatColor = None
        self.hTunicBodyColor = None
        self.hTunicSkirtColor = None
        self.zTunicHatColor = None
        
        self.zTunicHelmetColor = None
        self.zTunicBodyColor = None
        self.zTunicScalesColor = None
        self.zTunicBootsColor = None
        
        self.lanternGlowColor = None
        
        self.aBtnColor = None
        
        self.bBtnColor = None
        self.xBtnColor = None
        self.yBtnColor = None
        self.zBtnColor = None
        self.midnaHairBaseColor = None
        self.midnaHairTipsColor = None
        self.midnaDomeRingColor = None
        
        self.linkHairColor = None
        
    def _FileCreationSettings(self, bits):
        processor = BitsProcessor(bits)
             
        self.gameRegion = GameRegion(processor.NextInt(2))
        self.includeSpoilerLog = processor.NextBool()
        
        self.randomizeBgm = RandomizeBgm(processor.NextInt(2))
        self.randomizeFanfares = processor.NextBool()
        self.disableEnemyBgm = processor.NextBool()
        
        self.hTunicHatColor = 