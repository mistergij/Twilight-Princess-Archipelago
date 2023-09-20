import sys
from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


class RecolorId(Enum):
    Zero = 0xFFFF
    
    CMPR = 0x00
    
class RecolorType(Enum):
    Unknown = 0xFF
    Rgb = 0
    RgbArray = 1
    
class Clr0Result:
    def __init__(self, basicDataEntry, complexBytes):
        self.basicDataEntry = basicDataEntry
        self.complexBytes = complexBytes
    
class Clr0Entry(ABC):
    recolorId = RecolorId.Zero
    recolorType = RecolorType.Unknown
    
    @abstractmethod
    def getResult(self):
        pass
    

class Rgb:
    def __init__(self, r, g, b):
        # r, g, and b are bitstrings
        self.r = r
        self.g = g
        self.b = b

class RgbEntry(Clr0Entry):
    def __init__(self, recolorId, r, g, b):
        self.recolorType = RecolorType.Rgb
        self.recolorId = recolorId
        self.rgb = Rgb(r, g, b)
        
    def getResult(self):
        result = int(self.rgb.b, 2)
        result = (result) | (int(self.rgb.g, 2) << 8)
        result = (result) | (int(self.rgb.r, 2) << 16)
        
        return Clr0Result(result, None)

class CMPRTextureEntry:
    def __init__(self, rgb, textureName):
        self.rgb = rgb
        self.textureName = textureName

class CMPRTextureFileSettings:
    def __init__(self, colorEntry, bmdFile, texture, archiveIndex):
        self.colorEntry = colorEntry
        self.bmdFile = bmdFile
        self.texture = texture
        self.archiveIndex = archiveIndex

class BmdTextureAssociation:
    def __init__(self, recolorType, bmdFile, textures, archiveIndex):
        self.recolorType = recolorType
        self.bmdFile = bmdFile
        self.textures = textures
        self.archiveIndex = archiveIndex
        
class ArchiveIndex(Enum):
    Link = 0
    ZoraArmor = 1
    ZoraArmorField = 2

class ColorArrays:
    def __init__(self):
        self.MidnaBaseHairColors = [
            ["FFDC0000", "B4870000", "50000000"], # Default
            ["F5CFF300", "AD7F7F00", "1B002000"], # Pink
            ["E4654100", "A13E2200", "21000000"], # Red
            ["91830E00", "66500700", "0E0B0000"], # Yellow
            ["35795300", "254A2B00", "000E0500"],# Green
            ["0072FF00", "00468500", "00082800"], # Blue
            ["6F34FF00", "4E208500", "0D003400"], # Purple
            ["00000000", "00000000", "1A050000"], # Brown
            ["F0F1F100", "A9947E00", "090B0C00"], # White
            ["00000000", "00000000", "0B0B0B00"] # Black
        ]
        
        self.MidnaTipsHairColors = [
            ["00C3EB00", "C3C30000", "AAFFC300"], # Default
            ["DD00EB00", "DD00C300", "F64CFF00"], # Pink
            ["EB000000", "EB000000", "FF4F3A00"], # Red
            ["EBDE0000", "EBDE0000", "FFF8BF00"], # Yellow
            ["1FEB0000", "1FEB0000", "9AFF8100"], # Green
            ["0048EB00", "0048C300", "3A66FF00"], # Blue
            ["7B00EB00", "7B00C300", "943EFF00"], # Purple
            ["3F1D0B00", "3F1D0900", "59321E00"], # Brown
            ["EAEAEA00", "EAEAC200", "F3F3F300"], # White
            ["00000000", "00000000", "00000000"] # Black
        ]
        
        self.MidnaGlowHairColors = [
            ["00500000", "00000000", "00FF0078", "00000000", "00FF0064", "00780000"], # Default
            ["003C0002", "00580000", "00E30072", "00F20000", "00E3005F", "00F80000"], # Pink
            ["004F0002", "00010000", "00F0003A", "00250000", "00F00030", "008C0000"], # Red
            ["00240025", "00020000", "00CB00B7", "00000000", "00CB0099", "00780000"], # Yellow
            ["000A0029", "00100000", "000000B6", "006F0000", "00000098", "00B30000"], # Green
            ["0016001B", "005D0000", "00000060", "00FF0000", "00000050", "00FF0000"], # Blue
            ["00150008", "00790000", "00620000", "00FF0000", "00620000", "00FF0000"], # Purple
            ["003C0019", "000E0000", "003F001D", "000B0000", "003F0018", "007E0000"], # Brown
            ["00220024", "00240000", "00FF00FF", "00FF0000", "00FF00D5", "00FF0000"], # White
            ["00230023", "00230000", "00000000", "00000000", "00000000", "00780000"] # Black
        ]
