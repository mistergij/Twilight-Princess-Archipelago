from enum import Enum

class GameRegion(Enum):
    All = 0
    USA = 1
    EUR = 2
    JAP = 3

class RandomizeBgm(Enum):
    Off = 0
    Overworld = 1
    Dungeon = 2
    All = 3
    