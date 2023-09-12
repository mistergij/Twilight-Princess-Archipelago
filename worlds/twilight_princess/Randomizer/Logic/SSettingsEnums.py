from enum import Enum

class LogicRules(Enum):
    Glitchless = 0
    Glitched = 1
    No_Logic = 2

class CastleRequirements(Enum):
    Open = 0
    Fused_Shadows = 1
    Mirror_Shards = 2
    All_Dungeons = 3
    Vanilla = 4
    
class PalaceRequirements(Enum):
    Open = 0
    Fused_Shadows = 1
    Mirror_Shards = 2
    Vanilla = 3
    
class FaronWoodsLogic(Enum):
    Open = 0
    Closed = 1

class SmallKeySettings(Enum):
    Vanilla = 0
    Own_Dungeon = 1
    Any_Dungeon = 2
    Anywhere = 3
    Keysy = 4

class BigKeySettings(Enum):
    Vanilla = 0
    Own_Dungeon = 1
    Any_Dungeon = 2
    Anywhere = 3
    Start_With = 4
    
class TrapFrequency(Enum):
    Zero = 0 # Changed None to Zero due to python built-in type
    Few = 1
    Many = 2
    Mayhem = 3
    Nightmare = 4
    
class TotEntrance(Enum):
    Closed = 0
    OpenGrove = 1
    Open = 2
    
class GoronMinesEntrance:
    Closed = 0
    NoWrestling = 1
    Open = 2