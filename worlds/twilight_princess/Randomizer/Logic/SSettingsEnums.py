from enum import IntEnum

class LogicRules(IntEnum):
    Glitchless = 0
    Glitched = 1
    No_Logic = 2

class CastleRequirements(IntEnum):
    Open = 0
    Fused_Shadows = 1
    Mirror_Shards = 2
    All_Dungeons = 3
    Vanilla = 4
    
class PalaceRequirements(IntEnum):
    Open = 0
    Fused_Shadows = 1
    Mirror_Shards = 2
    Vanilla = 3
    
class FaronWoodsLogic(IntEnum):
    Open = 0
    Closed = 1

class SmallKeySettings(IntEnum):
    Vanilla = 0
    Own_Dungeon = 1
    Any_Dungeon = 2
    Anywhere = 3
    Keysy = 4

class BigKeySettings(IntEnum):
    Vanilla = 0
    Own_Dungeon = 1
    Any_Dungeon = 2
    Anywhere = 3
    Start_With = 4
    
class MapAndCompassSettings(IntEnum):
    Vanilla = 0
    Own_Dungeon = 1
    Any_Dungeon = 2
    Anywhere = 3
    Start_With = 4
    
class TrapFrequency(IntEnum):
    Zero = 0 # Changed None to Zero due to python built-in type
    Few = 1
    Many = 2
    Mayhem = 3
    Nightmare = 4
    
class TotEntrance(IntEnum):
    Closed = 0
    OpenGrove = 1
    Open = 2
    
class GoronMinesEntrance(IntEnum):
    Closed = 0
    NoWrestling = 1
    Open = 2