from typing import NamedTuple, Optional, Dict
from BaseClasses import Location


class AchievementData(NamedTuple):
    id: Optional[int]
    region: str


class TwilightPrincessAchievement(Location):
    game: str = "Twilight Princess"


achievement_table: Dict[str, AchievementData] = {
    "Wooden Sword Chest": AchievementData(0x4770000, "Inside Link's House"),
    "Links Basement Chest": AchievementData(0x4770001, "Inside Link's House"),
    "Ordon Ranch Grotto Lantern Chest": AchievementData(
        0x4770002, "Ordon Ranch Grotto"
    ),
    "Faron Field Bridge Chest": AchievementData(
        0x4770003, "Hyrule Field - Faron Field"
    ),
    "Faron Field Corner Grotto Left Chest": AchievementData(
        0x4770004, "Hyrule Field - Faron Field"
    ),
    "Faron Field Corner Grotto Rear Chest": AchievementData(
        0x4770005, "Hyrule Field - Faron Field"
    ),
    "Faron Field Corner Grotto Right Chest": AchievementData(
        0x4770006, "Hyrule Field - Faron Field"
    ),
    "Faron Mist Cave Lantern Chest": AchievementData(0x4770007, "Faron Mist Cave"),
    "Faron Mist Cave Open Chest": AchievementData(0x4770008, "Faron Mist Cave"),
    "Faron Mist North Chest": AchievementData(0x4770009, "Faron Mist Area"),
    "Faron Mist South Chest": AchievementData(0x477000A, "Faron Mist Area"),
    "Faron Mist Stump Chest": AchievementData(0x477000B, "Faron Mist Area"),
    "Faron Woods Owl Statue Chest": AchievementData(0x477000C, "Faron Mist Area"),
    "Lost Woods Lantern Chest": AchievementData(0x477000D, "Lost Woods"),
    "North Faron Woods Deku Baba Chest": AchievementData(
        0x477000E, "North Faron Woods"
    ),
    "Sacred Grove Baba Serpent Grotto Chest": AchievementData(0x477000F, "Lost Woods"),
    "Sacred Grove Past Owl Statue Chest": AchievementData(
        0x4770010, "Sacred Grove - Temple of Time"
    ),
    "Sacred Grove Spinner Chest": AchievementData(0x4770011, "Lost Woods"),
    "South Faron Cave Chest": AchievementData(0x4770012, "South Faron Woods Mist Cave"),
    "Bridge of Eldin Owl Statue Chest": AchievementData(
        0x4770013, "Hyrule Field - Eldin Field"
    ),
    "Death Mountain Alcove Chest": AchievementData(0x4770014, "Death Mountain"),
    "Eldin Field Bomb Rock Crash": AchievementData(
        0x4770015, "Hyrule Field - Eldin Field"
    ),
    "Eldin Field Bomskit Grotto Lantern Chest": AchievementData(
        0x4770016, "Hyrule Field - Eldin Field"
    ),
    "Eldin Field Bomskit Grotto Left Chest": AchievementData(
        0x4770017, "Hyrule Field - Eldin Field"
    ),
    "Eldin Field Stalfos Grotto Left Small Chest": AchievementData(
        0x4770018, "Hyrule Field - Eldin Field"
    ),
    "Eldin Field Stalfos Grotto Right Small Chest": AchievementData(
        0x4770019, "Hyrule Field - Eldin Field"
    ),
    "Eldin Field Stalfos Grotto Stalfos Chest": AchievementData(
        0x477001A, "Hyrule Field - Eldin Field"
    ),
    "Eldin Lantern Cave First Chest": AchievementData(0x477001B, "Eldin Lantern Cave"),
    "Eldin Lantern Cave Lantern Chest": AchievementData(
        0x477001C, "Eldin Lantern Cave"
    ),
    "Eldin Lantern Cave Second Chest": AchievementData(0x477001D, "Eldin Lantern Cave"),
    "Eldin Spring Underwater Cave": AchievementData(0x477001E, "Kakariko Village"),
    "Eldin Stockcave Lantern Chest": AchievementData(0x477001F, "Eldin Stockcave"),
    "Eldin Stockcave Lowest Chest": AchievementData(0x4770020, "Eldin Stockcave"),
    "Eldin Stockcave Upper Chest": AchievementData(0x4770021, "Eldin Stockcave"),
    "Kakariko Gorge Double Clawshot Chest": AchievementData(
        0x4770022, "Hyrule Field - Kakariko Gorge"
    ),
    "Kakariko Gorge Owl Statue Chest": AchievementData(
        0x4770023, "Hyrule Field - Kakariko Gorge"
    ),
    "Kakariko Graveyard Lantern Chest": AchievementData(
        0x4770024, "Kakariko Graveyard"
    ),
    "Kakariko Inn Chest": AchievementData(0x4770025, "Kakariko Village"),
    "Kakariko Watchtower Alcove Chest": AchievementData(0x4770026, "Kakariko Village"),
    "Kakariko Watchtower Chest": AchievementData(0x4770027, "Kakariko Village"),
    "Doctors Office Balcony Chest": AchievementData(0x4770028, "Castle Town"),
    "Fishing Hole Bottle": AchievementData(0x4770028, "Fishing Hole"),
    "Flight By Fowl Fifth Platform Chest": AchievementData(0x4770029, "Lake Hylia"),
    "Flight By Fowl Fourth Platform Chest": AchievementData(0x477002A, "Lake Hylia"),
    "Flight By Fowl Second Platform Chest": AchievementData(0x477002B, "Lake Hylia"),
    "Flight By Fowl Third Platform Chest": AchievementData(0x477002C, "Lake Hylia"),
    "Flight By Fowl Top Platform Chest": AchievementData(0x477002D, "Lake Hylia"),
}
