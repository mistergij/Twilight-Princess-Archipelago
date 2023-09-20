import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from Logic.LogicFunctions import LogicFunctions as lgf


class Randomizer():
    Logic = lgf()
    
    def __init__(self):
        self.RequiredDungeons = 0

    def CreateInputJson(
        self,
        idParam,
        settingsString,
        raceSeedParam,
        seed
        ):
            pass
        