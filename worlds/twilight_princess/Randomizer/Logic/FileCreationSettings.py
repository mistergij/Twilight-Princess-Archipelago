import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from Util.SettingsEncoder import BitsProcessor
from Util.SettingsEncoder import SettingsEncoder
from FcSettingsEnums import GameRegion, RandomizeBgm
from Assets.CLR0.clr0Types import RecolorId


class FileCreationSettings:
    def __init__(self, bits):
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
        
        self.heartColor = None
        
        self.aBtnColor = None
        
        self.bBtnColor = None
        self.xBtnColor = None
        self.yBtnColor = None
        self.zBtnColor = None
        self.midnaHairBaseColor = None
        self.midnaHairTipsColor = None
        self.midnaDomeRingColor = None
        
        self.linkHairColor = None
        
        self.processor = BitsProcessor(bits)
        
    def _FileCreationSettings(self, bits):
        processor = BitsProcessor(bits)
             
        self.gameRegion = GameRegion(processor.NextInt(2))
        self.includeSpoilerLog = processor.NextBool()
        
        self.randomizeBgm = RandomizeBgm(processor.NextInt(2))
        self.randomizeFanfares = processor.NextBool()
        self.disableEnemyBgm = processor.NextBool()
        
        self.hTunicHatColor = processor.NextClr0Entry(RecolorId.CMPR)
        self.hTunicBodyColor = processor.NextClr0Entry(RecolorId.CMPR)
        self.hTunicSkirtColor = processor.NextClr0Entry(RecolorId.CMPR)
        self.zTunicHatColor = processor.NextClr0Entry(RecolorId.CMPR)
        self.zTunicHelmetColor = processor.NextClr0Entry(RecolorId.CMPR)
        self.zTunicBodyColor = processor.NextClr0Entry(RecolorId.CMPR)
        self.zTunicScalesColor = processor.NextClr0Entry(RecolorId.CMPR)
        self.zTunicBootsColor = processor.NextClr0Entry(RecolorId.CMPR)
        self.lanternGlowColor = processor.NextClr0Entry(RecolorId.Zero)
        self.heartColor = processor.NextClr0Entry(RecolorId.Zero)
        self.aBtnColor = processor.NextClr0Entry(RecolorId.Zero)
        self.bBtnColor = processor.NextClr0Entry(RecolorId.Zero)
        self.xBtnColor = processor.NextClr0Entry(RecolorId.Zero)
        self.yBtnColor = processor.NextClr0Entry(RecolorId.Zero)
        self.zBtnColor = processor.NextClr0Entry(RecolorId.Zero)
        self.midnaHairBaseColor = processor.NextInt(4)
        self.midnaHairTipsColor = processor.NextInt(4)
        self.midnaDomeRingColor = processor.NextInt(4)
        self.linkHairColor = processor.NextClr0Entry(RecolorId.CMPR)
        
    def FromString(self, fcSettingsString):
        bits = SettingsEncoder().DecodeToBitString(fcSettingsString)
        fcs = FileCreationSettings()
        fcs._FileCreationSettings(bits)
        return fcs
