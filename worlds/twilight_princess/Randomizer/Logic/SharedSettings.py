from SSettingsEnums import (BigKeySettings, CastleRequirements,
                            FaronWoodsLogic, GoronMinesEntrance, LogicRules,
                            MapAndCompassSettings, PalaceRequirements,
                            SmallKeySettings, TotEntrance, TrapFrequency)


class SharedSettings:
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
    