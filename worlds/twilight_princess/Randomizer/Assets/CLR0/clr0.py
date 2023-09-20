class Clr0EntryComparer:
#TODO: Implement CLR0EntryComparer?
    pass

class CLR0:
    def BuildClr0(self, fCSettings):
        cmprTextureList = []
        rawRGBList = []
        clr0Raw = []
        bmdListRaw = []
        textureListRaw = []
        textureAssociations = []
        clr0HeaderSize = 0xC
        cmprFileModifications = []
        entries = []
        
        #TODO: Implement FileCreationSettings class in Logic/FileCreationSettings