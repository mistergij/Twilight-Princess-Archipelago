from BaseClasses import Location
from typing import NamedTuple, Optional, Dict


class AchievementData(NamedTuple):
    id: Optional[int]
    region: str


class TwilightPrincessAchievement(Location):
    game: str = "Twilight Princess"


achievement_table: Dict[str, AchievementData] = {
    
}
