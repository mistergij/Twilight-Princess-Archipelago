from SSettingsEnums import (BigKeySettings, CastleRequirements,
                            FaronWoodsLogic, GoronMinesEntrance, LogicRules,
                            MapAndCompassSettings, PalaceRequirements,
                            SmallKeySettings, TotEntrance, TrapFrequency)


class SharedSettings:
#TODO: Implement SSettingsEnums
    def __init__(self):
        self._logicRules = LogicRules
        self._castleRequirements = CastleRequirements
        self._palaceRequirements = PalaceRequirements
        self._faronWoodsLogic = FaronWoodsLogic
        self.shuffleGoldenBugs = False
        self.shuffleSkyCharacters = False
        self.shuffleNpcItems = False
        self.shufflePoes = False
        self.shuffleShopItems = False
        self.shuffleHiddenSkills = False
        self._smallKeySettings = SmallKeySettings
        self._bigKeySettings = BigKeySettings
        self._mapAndCompassSettings = MapAndCompassSettings
        self.skipPrologue = True
        self.faronTwilightCleared = False
        self.eldinTwilightCleared = False
        self.lanayruTwilightCleared = False
        self.skipMdh = True
        self.skipMinorCutscenes = False
        self.fastIronBoots = False
        self.quickTransform = False
        self.transformAnywhere = False
        self.increaseWallet = True
        self.modifyShopModels = True
        self._trapFrequency = TrapFrequency
        self.barrenDungeons = False
        self._goronMinesEntrance = GoronMinesEntrance
        self.skipLakebedEntrance = False
        self.skipArbitersEntrance = False
        self.skipSnowpeakEntrance = False
        self._totEntrance = TotEntrance
        self.skipCityEntrance = False
        self.instantText = True
        self.openMap = False
        self.increaseSpinnerSpeed = False
        self.openDot = False
        self.startingItems = []
        self.excludedChecks = []
        
    @property
    def logicRules(self):
        return self._logicRules
    
    @logicRules.setter
    def logicRules(self, value):
        self._logicRules = value
    
    @property
    def castleRequirements(self):
        return self._castleRequirements
    
    @castleRequirements.setter
    def castleRequirements(self, value):
        self._castleRequirements = value
        
    @property
    def palaceRequirements(self):
        return self._castleRequirements
    
    @palaceRequirements.setter
    def palaceRequirements(self, value):
        self._palaceRequirements = value
    
    @property
    def faronWoodsLogic(self):
        return self._faronWoodsLogic
    
    @faronWoodsLogic.setter
    def faronWoodsLogic(self, value):
        self._faronWoodsLogic = value
        
    @property
    def smallKeySettings(self):
        return self._smallKeySettings
    
    @smallKeySettings.setter
    def smallKeySettings(self, value):
        self._smallKeySettings = value
    
    @property
    def bigKeySettings(self):
        return self._bigKeySettings
    
    @bigKeySettings.setter
    def bigKeySettings(self, value):
        self._bigKeySettings = value
        
    @property
    def mapAndCompassSettings(self):
        return self._mapAndCompassSettings
    
    @mapAndCompassSettings.setter
    def mapAndCompassSettings(self, value):
        self._mapAndCompassSettings = value
    
    @property
    def trapFrequency(self):
        return self._trapFrequency
    
    @trapFrequency.setter
    def trapFrequency(self, value):
        self._trapFrequency = value
        
    @property
    def goronMinesEntrance(self):
        return self._goronMinesEntrance
    
    @goronMinesEntrance.setter
    def goronMinesEntrance(self, value):
        self._goronMinesEntrance = value
        
    @property
    def totEntrance(self):
        return self._totEntrance
    
    @totEntrance.setter
    def totEntrance(self, value):
        self._totEntrance = value

    def SharedSettings(self):
        pass
    
    