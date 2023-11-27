import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from clr0Types import (ArchiveIndex, BmdTextureAssociation, CMPRTextureEntry,
                       CMPRTextureFileSettings, RecolorId, RgbEntry)
from Logic import FileCreationSettings
from Assets.Converter import Converter

class CLR0:
    def BuildClr0(self, fcSettings):
        cmprTextureList = []
        rawRGBList = []
        clr0Raw = []
        rawRGBRaw = []
        bmdListRaw = []
        textureListRaw = []
        textureAssociations = []
        clr0HeaderSize = 0xC
        cmprFileModifications = []
        entries = []
        
        # Link
        # Hero's Tunic
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.hTunicSkirtColor, "al.bmd", "al_lowbody", ArchiveIndex.Link.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.hTunicBodyColor, "al.bmd", "al_upbody", ArchiveIndex.Link.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.hTunicHatColor, "al_head.bmd", "al_cap", ArchiveIndex.Link.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.linkHairColor, "al_head.bmd", "al_hair", ArchiveIndex.Link.value))
        
        # Zora Armor
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.zTunicHatColor, "zl_head.bmd", "zl_cap", ArchiveIndex.ZoraArmor.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.zTunicHelmetColor, "zl_head.bmd", "zl_helmet", ArchiveIndex.ZoraArmor.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.zTunicBodyColor, "zl.bmd", "zl_armor", ArchiveIndex.ZoraArmor.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.zTunicScalesColor, "zl.bmd", "zl_body", ArchiveIndex.ZoraArmor.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.zTunicBootsColor, "zl.bmd", "zl_boots", ArchiveIndex.ZoraArmor.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.zTunicBodyColor, "zl.bmd", "zl_armL", ArchiveIndex.ZoraArmor.value))
        
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.zTunicBodyColor, "o_gd_al_zora.bmd", "zl_armor", ArchiveIndex.ZoraArmorField.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.zTunicScalesColor, "o_gd_al_zora.bmd", "z1_body", ArchiveIndex.ZoraArmorField.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.zTunicHelmetColor, "o_gd_al_zora.bmd", "zl_helmet", ArchiveIndex.ZoraArmorField.value))
        cmprFileModifications.append(CMPRTextureFileSettings(fcSettings.zTunicHatColor, "o_gd_al_zora.bmd", "zl_cap", ArchiveIndex.ZoraArmorField.value))
        
        entries.append(fcSettings.hTunicHatColor)
        entries.append(fcSettings.hTunicBodyColor)
        entries.append(fcSettings.hTunicSkirtColor)
        entries.append(fcSettings.zTunicHatColor)
        entries.append(fcSettings.zTunicHelmetColor)
        entries.append(fcSettings.zTunicBodyColor)
        entries.append(fcSettings.zTunicScalesColor)
        entries.append(fcSettings.zTunicBootsColor)
        entries.append(fcSettings.lanternGlowColor)
        entries.append(fcSettings.heartColor)
        entries.append(fcSettings.aBtnColor)
        entries.append(fcSettings.bBtnColor)
        entries.append(fcSettings.xBtnColor)
        entries.append(fcSettings.yBtnColor)
        entries.append(fcSettings.zBtnColor)
        entries.append(fcSettings.midnaDomeRingColor)
        entries.append(fcSettings.linkHairColor)
        
        for entry in entries:
            if entry != None:
                match entry.recolorId.value:
                    case RecolorId.Zero.value:
                        result = entry.getResult()
                        rawRGBList.append(((result.basicDataEntry << 0x8) | 0xFF))
                        break
                    
                    case RecolorId.CMPR.value:
                        for modification in cmprFileModifications:
                            if modification.colorEntry != None:
                                if modification.colorEntry == entry:
                                    if len(textureAssociations) > 0:
                                        isInList = False
                                        for association in textureAssociations:
                                            if modification.bmdFile == association.bmdFile:
                                                association.textures.append(modification.texture)
                                                isInList = True
                                                break
                                        
                                        if not isInList:
                                            newAssociation = BmdTextureAssociation(
                                                RecolorId.CMPR.value,
                                                modification.bmdFile,
                                                [],
                                                modification.archiveIndex
                                            )
                                            newAssociation.textures.append(modification.texture)
                                            textureAssociations.append(newAssociation)
                                            
                                    else:
                                        newAssociation = BmdTextureAssociation(
                                            RecolorId.CMPR.value,
                                            modification.bmdFile,
                                            [],
                                            modification.archiveIndex
                                        )
                                        newAssociation.textures.append(modification.texture)
                                        textureAssociations.append(newAssociation)
                                        
                                    result = entry.getResult()
                                    cmprTextureList.append(CMPRTextureEntry(result.basicDataEntry, modification.texture))
                                    
                    case _:
                        print("Invalid recolor id: " + entry.recolorId.value)
                        break
                    
        for association in textureAssociations:
            bmdListRaw.append(Converter.GcByte(association.recolorType))
            bmdListRaw.append(Converter.GcByte(association.archiveIndex))
            bmdListRaw.extend(Converter.GcBytesBigEndian16(association.textures.Count))
            bmdListRaw.extend(
                Converter.GcBytesBigEndian16(
                    int(
                        (len(textureAssociations * 0x18))
                        + clr0HeaderSize
                        + len(textureListRaw)
                    )
                )
            )
            bmdListRaw.extend(Converter.StringBytes(association.bmdFile, 0x12))
            
            for texture in association.textures:
                for modification in cmprFileModifications:
                    if (modification.texture == texture) and (modification.archiveIndex == association.archiveIndex):
                        result = modification.colorEntry.getResult()
                        textureListRaw.extend(
                            Converter.GcBytesBigEndian32((result.basicDataEntry << 0x8) | 0xFF)
                        )
                        textureListRaw.extend(Converter.StringBytes(texture, 0xC))
        
        for rawRGB in rawRGBList:
            rawRGBRaw.extend(Converter.GcBytesBigEndian32(rawRGB))
            
        clr0Raw.extend(
            Converter.GcBytesBigEndian32(
                clr0HeaderSize + len(bmdListRaw) + len(textureListRaw) + len(rawRGBRaw)
            )
        )
        clr0Raw.extend(Converter.GcBytesBigEndian32(len(textureAssociations)))
        clr0Raw.extend(Converter.GcBytesBigEndian16(clr0HeaderSize))
        clr0Raw.extend(
            Converter.GcBytesBigEndian16(
                clr0HeaderSize + len(bmdListRaw) + len(textureListRaw)
            )
        )
        clr0Raw.extend(bmdListRaw)
        clr0Raw.extend(textureListRaw)
        clr0Raw.extend(rawRGBRaw)
        
        return clr0Raw