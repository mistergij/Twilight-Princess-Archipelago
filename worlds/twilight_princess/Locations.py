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
    "Eldin Field Bomb Rock Chest": AchievementData(
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
    "Eldin Spring Underwater Chest": AchievementData(0x477001E, "Kakariko Village"),
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
    "Flight By Fowl Top Platform Reward": AchievementData(0x477002D, "Lake Hylia"),
    "Hyrule Field Ampitheater Owl Statue Chest": AchievementData(
        0x477002E, "Hyrule Field - Outside West Castle Town"
    ),
    "Lake Hylia Bridge Bubble Grotto Chest": AchievementData(
        0x477002F, "Hyrule Field - Lake Hylia Bridge"
    ),
    "Lake Hylia Bridge Cliff Chest": AchievementData(
        0x4770030, "Hyrule Field - Lake Hylia Bridge"
    ),
    "Lake Hylia Bridge Owl Statue Chest": AchievementData(
        0x4770031, "Hyrule Field - Lake Hylia Bridge"
    ),
    "Lake Hylia Bridge Vines Chest": AchievementData(
        0x4770032, "Hyrule Field - Lake Hylia Bridge"
    ),
    "Lake Hylia Shell Blade Grotto Chest": AchievementData(0x4770033, "Lake Hylia"),
    "Lake Hylia Underwater Chest": AchievementData(0x4770034, "Lake Hylia"),
    "Lake Hylia Water Toadpoli Grotto Chest": AchievementData(0x4770035, "Lake Hylia"),
    "Lake Lantern Cave Eighth Chest": AchievementData(0x4770036, "Lake Lantern Cave"),
    "Lake Lantern Cave Eleventh Chest": AchievementData(0x4770037, "Lake Lantern Cave"),
    "Lake Lantern Cave End Lantern Chest": AchievementData(
        0x4770038, "Lake Lantern Cave"
    ),
    "Lake Lantern Cave Fifth Chest": AchievementData(0x4770039, "Lake Lantern Cave"),
    "Lake Lantern Cave First Chest": AchievementData(0x477003A, "Lake Lantern Cave"),
    "Lake Lantern Cave Fourteenth Chest": AchievementData(
        0x477003B, "Lake Lantern Cave"
    ),
    "Lake Lantern Cave Fourth Chest": AchievementData(0x477003C, "Lake Lantern Cave"),
    "Lake Lantern Cave Ninth Chest": AchievementData(0x477003D, "Lake Lantern Cave"),
    "Lake Lantern Cave Second Chest": AchievementData(0x477003E, "Lake Lantern Cave"),
    "Lake Lantern Cave Seventh Chest": AchievementData(0x477003F, "Lake Lantern Cave"),
    "Lake Lantern Cave Sixth Chest": AchievementData(0x4770040, "Lake Lantern Cave"),
    "Lake Lantern Cave Tenth Chest": AchievementData(0x4770041, "Lake Lantern Cave"),
    "Lake Lantern Cave Third Chest": AchievementData(0x4770042, "Lake Lantern Cave"),
    "Lake Lantern Cave Thirteenth Chest": AchievementData(
        0x4770043, "Lake Lantern Cave"
    ),
    "Lake Lantern Cave Twelfth Chest": AchievementData(0x4770044, "Lake Lantern Cave"),
    "Lanayru Field Behind Gate Underwater Chest": AchievementData(
        0x4770045, "Hyrule Field - Lanayru Field"
    ),
    "Lanayru Field Skulltula Grotto Chest": AchievementData(
        0x4770046, "Hyrule Field - Lanayru Field"
    ),
    "Lanayru Field Spinner Track Chest": AchievementData(
        0x4770047, "Hyrule Field - Lanayru Field"
    ),
    "Lanayru Ice Block Puzzle Cave Chest": AchievementData(
        0x4770048, "Hyrule Field - Lanayru Ice Puzzle Cave"
    ),
    "Lanayru Spring Back Room Lantern Chest": AchievementData(0x4770049, "Lake Hylia"),
    "Lanayru Spring Back Room Left Chest": AchievementData(0x477004A, "Lake Hylia"),
    "Lanayru Spring Back Room Right Chest": AchievementData(0x477004B, "Lake Hylia"),
    "Lanayru Spring East Double Clawshot Chest": AchievementData(
        0x477004C, "Lake Hylia"
    ),
    "Lanayru Spring Underwater Left Chest": AchievementData(0x477004D, "Lake Hylia"),
    "Lanayru Spring Underwater Right Chest": AchievementData(0x477004E, "Lake Hylia"),
    "Lanayru Spring West Double Clawshot Chest": AchievementData(
        0x477004F, "Lake Hylia"
    ),
    "Outside Lanayru Spring Left Statue Chest": AchievementData(
        0x4770050, "Lake Hylia"
    ),
    "Outside Lanayru Spring Right Statue Chest": AchievementData(
        0x4770051, "Lake Hylia"
    ),
    "Outside South Castle Town Double Clawshot Chasm Chest": AchievementData(
        0x4770052, "Hyrule Field - Outside South Castle Town"
    ),
    "Outside South Castle Town Fountain Chest": AchievementData(
        0x4770053, "Hyrule Field - Outside South Castle Town"
    ),
    "Outside South Castle Town Tektite Grotto Chest": AchievementData(
        0x4770054, "Hyrule Field - Outside South Castle Town"
    ),
    "Outside South Castle Town Tightrope Chest": AchievementData(
        0x4770055, "Hyrule Field - Outside South Castle Town"
    ),
    "West Hyrule Field Helmasaur Grotto Chest": AchievementData(
        0x4770056, "Hyrule Field - Outside West Castle Town"
    ),
    "Wooden Statue": AchievementData(
        0x4770057, "Hyrule Field - Outside South Castle Town"
    ),
    "Zoras Domain Chest Behind Waterfall": AchievementData(0x4770058, "Zoras Domain"),
    "Zoras Domain Chest By Mother and Child Isles": AchievementData(
        0x4770059, "Zoras Domain"
    ),
    "Zoras Domain Extinguish All Torches Chest": AchievementData(
        0x477005A, "Zoras Domain"
    ),
    "Zoras Domain Light All Torches Chest": AchievementData(0x477005B, "Zoras Domain"),
    "Snowpeak Cave Ice Lantern Chest": AchievementData(0x477005C, "Snowpeak"),
    "Snowpeak Freezard Grotto Chest": AchievementData(0x477005D, "Snowpeak"),
    "Bulblin Camp First Chest Under Tower At Entrance": AchievementData(
        0x477005E, "Bulblin Camp"
    ),
    "Bulblin Camp Small Chest in Back of Camp": AchievementData(
        0x477005F, "Bulblin Camp"
    ),
    "Gerudo Desert Campfire East Chest": AchievementData(0x4770060, "Gerudo Desert"),
    "Gerudo Desert Campfire North Chest": AchievementData(0x4770061, "Gerudo Desert"),
    "Gerudo Desert Campfire West Chest": AchievementData(0x4770062, "Gerudo Desert"),
    "Gerudo Desert East Canyon Chest": AchievementData(0x4770063, "Gerudo Desert"),
    "Gerudo Desert Lone Small Chest": AchievementData(0x4770064, "Gerudo Desert"),
    "Gerudo Desert North Small Chest Before Bulblin Camp": AchievementData(
        0x4770065, "Gerudo Desert"
    ),
    "Gerudo Desert Northeast Chest Behind Gates": AchievementData(
        0x4770066, "Gerudo Desert"
    ),
    "Gerudo Desert Northwest Chest Behind Gates": AchievementData(
        0x4770067, "Gerudo Desert"
    ),
    "Gerudo Desert Owl Statue Chest": AchievementData(0x4770068, "Gerudo Desert"),
    "Gerudo Desert Peahat Ledge Chest": AchievementData(0x4770069, "Gerudo Desert"),
    "Gerudo Desert Rock Grotto Lantern Chest": AchievementData(
        0x477006A, "Gerudo Desert"
    ),
    "Gerudo Desert Skulltula Grotto Chest": AchievementData(0x477006B, "Gerudo Desert"),
    "Gerudo Desert South Chest Behind Wooden Gates": AchievementData(
        0x477006C, "Gerudo Desert"
    ),
    "Gerudo Desert West Canyon Chest": AchievementData(0x477006D, "Gerudo Desert"),
    "Outside Arbiters Grounds Lantern Chest": AchievementData(
        0x477006E, "Bulblin Camp"
    ),
    "Forest Temple Big Baba Key": AchievementData(0x477006F, "Forest Temple"),
    "Forest Temple Big Key Chest": AchievementData(0x4770070, "Forest Temple"),
    "Forest Temple Central Chest Behind Stairs": AchievementData(
        0x4770071, "Forest Temple"
    ),
    "Forest Temple Central Chest Hanging From Web": AchievementData(
        0x4770072, "Forest Temple"
    ),
    "Forest Temple Central North Chest": AchievementData(0x4770073, "Forest Temple"),
    "Forest Temple Dungeon Reward": AchievementData(0x4770074, "Forest Temple"),
    "Forest Temple East Tile Worm Chest": AchievementData(0x4770075, "Forest Temple"),
    "Forest Temple East Water Cave Chest": AchievementData(0x4770076, "Forest Temple"),
    "Forest Temple Diababa Heart Container": AchievementData(
        0x4770077, "Forest Temple"
    ),
    "Forest Temple Entrance Vines Chest": AchievementData(0x4770078, "Forest Temple"),
    "Forest Temple Gale Boomerang": AchievementData(0x4770079, "Forest Temple"),
    "Forest Temple North Deku Like Chest": AchievementData(0x477007A, "Forest Temple"),
    "Forest Temple Second Monkey Under Bridge Chest": AchievementData(
        0x477007B, "Forest Temple"
    ),
    "Forest Temple Totem Pole Chest": AchievementData(0x477007C, "Forest Temple"),
    "Forest Temple West Deku Like Chest": AchievementData(0x477007D, "Forest Temple"),
    "Forest Temple West Tile Worm Chest Behind Stairs": AchievementData(
        0x477007E, "Forest Temple"
    ),
    "Forest Temple West Tile Worm Room Vines Chest": AchievementData(
        0x477007F, "Forest Temple"
    ),
    "Forest Temple Windless Bridge Chest": AchievementData(0x4770080, "Forest Temple"),
    "Goron Mines After Crystal Switch Room Magnet Wall Chest": AchievementData(
        0x4770081, "Goron Mines"
    ),
    "Goron Mines Beamos Room Chest": AchievementData(0x4770082, "Goron Mines"),
    "Goron Mines Chest Before Dangoro": AchievementData(0x4770083, "Goron Mines"),
    "Goron Mines Crystal Switch Room Small Chest": AchievementData(
        0x4770084, "Goron Mines"
    ),
    "Goron Mines Crystal Switch Room Underwater Chest": AchievementData(
        0x4770085, "Goron Mines"
    ),
    "Goron Mines Dangoro Chest": AchievementData(0x4770086, "Goron Mines"),
    "Goron Mines Dungeon Reward": AchievementData(0x4770087, "Goron Mines"),
    "Goron Mines Entrance Chest": AchievementData(0x4770088, "Goron Mines"),
    "Goron Mines Fyrus Heart Container": AchievementData(0x4770089, "Goron Mines"),
    "Goron Mines Gor Amato Chest": AchievementData(0x477008A, "Goron Mines"),
    "Goron Mines Gor Amato Key Shard": AchievementData(0x477008B, "Goron Mines"),
    "Goron Mines Gor Amato Small Chest": AchievementData(0x477008C, "Goron Mines"),
    "Goron Mines Gor Ebizo Chest": AchievementData(0x477008D, "Goron Mines"),
    "Goron Mines Gor Ebizo Key Shard": AchievementData(0x477008E, "Goron Mines"),
    "Goron Mines Gor Liggs Chest": AchievementData(0x477008F, "Goron Mines"),
    "Goron Mines Gor Liggs Key Shard": AchievementData(0x4770090, "Goron Mines"),
    "Goron Mines Magnet Maze Chest": AchievementData(0x4770091, "Goron Mines"),
    "Goron Mines Main Magnet Room Bottom Chest": AchievementData(
        0x4770092, "Goron Mines"
    ),
    "Goron Mines Main Magnet Room Top Chest": AchievementData(0x4770093, "Goron Mines"),
    "Goron Mines Outside Beamos Chest": AchievementData(0x4770094, "Goron Mines"),
    "Goron Mines Outside Clawshot Chest": AchievementData(0x4770095, "Goron Mines"),
    "Goron Mines Outside Underwater Chest": AchievementData(0x4770096, "Goron Mines"),
    "Lakebed Temple Before Deku Toad Alcove Chest": AchievementData(
        0x4770097, "Lakebed Temple"
    ),
    "Lakebed Temple Before Deku Toad Underwater Left Chest": AchievementData(
        0x4770098, "Lakebed Temple"
    ),
    "Lakebed Temple Before Deku Toad Underwater Right Chest": AchievementData(
        0x4770099, "Lakebed Temple"
    ),
    "Lakebed Temple Big Key Chest": AchievementData(0x477009A, "Lakebed Temple"),
    "Lakebed Temple Central Room Chest": AchievementData(0x477009B, "Lakebed Temple"),
    "Lakebed Temple Central Room Small Chest": AchievementData(
        0x477009C, "Lakebed Temple"
    ),
    "Lakebed Temple Central Room Spire Chest": AchievementData(
        0x477009D, "Lakebed Temple"
    ),
    "Lakebed Temple Chandelier Chest": AchievementData(0x477009E, "Lakebed Temple"),
    "Lakebed Temple Deku Toad Chest": AchievementData(0x477009F, "Lakebed Temple"),
    "Lakebed Temple Dungeon Reward": AchievementData(0x47700A0, "Lakebed Temple"),
    "Lakebed Temple East Lower Waterwheel Bridge Chest": AchievementData(
        0x47700A1, "Lakebed Temple"
    ),
    "Lakebed Temple East Lower Waterwheel Stalactite Chest": AchievementData(
        0x47700A2, "Lakebed Temple"
    ),
    "Lakebed Temple East Second Floor Southeast Chest": AchievementData(
        0x47700A3, "Lakebed Temple"
    ),
    "Lakebed Temple East Second Floor Southwest Chest": AchievementData(
        0x47700A4, "Lakebed Temple"
    ),
    "Lakebed Temple East Water Supply Clawshot Chest": AchievementData(
        0x47700A5, "Lakebed Temple"
    ),
    "Lakebed Temple East Water Supply Small Chest": AchievementData(
        0x47700A6, "Lakebed Temple"
    ),
    "Lakebed Temple Lobby Left Chest": AchievementData(0x47700A7, "Lakebed Temple"),
    "Lakebed Temple Lobby Rear Chest": AchievementData(0x47700A8, "Lakebed Temple"),
    "Lakebed Temple Morpheel Heart Container": AchievementData(
        0x47700A9, "Lakebed Temple"
    ),
    "Lakebed Temple Stalactite Room Chest": AchievementData(
        0x47700AA, "Lakebed Temple"
    ),
    "Lakebed Temple Underwater Maze Small Chest": AchievementData(
        0x47700AB, "Lakebed Temple"
    ),
    "Lakebed Temple West Lower Small Chest": AchievementData(
        0x47700AC, "Lakebed Temple"
    ),
    "Lakebed Temple West Second Floor Central Small Chest": AchievementData(
        0x47700AD, "Lakebed Temple"
    ),
    "Lakebed Temple West Second Floor Northeast Chest": AchievementData(
        0x47700AE, "Lakebed Temple"
    ),
    "Lakebed Temple West Second Floor Southeast Chest": AchievementData(
        0x47700AF, "Lakebed Temple"
    ),
    "Lakebed Temple West Second Floor Southwest Underwater Chest": AchievementData(
        0x47700B0, "Lakebed Temple"
    ),
    "Lakebed Temple West Water Supply Chest": AchievementData(
        0x47700B1, "Lakebed Temple"
    ),
    "Lakebed Temple West Water Supply Small Chest": AchievementData(
        0x47700B2, "Lakebed Temple"
    ),
    "Arbiters Grounds Big Key Chest": AchievementData(0x47700B3, "Arbiters Grounds"),
    "Arbiters Grounds Death Sword Chest": AchievementData(
        0x47700B4, "Arbiters Grounds"
    ),
    "Arbiters Grounds East Lower Turnable Redead Chest": AchievementData(
        0x47700B5, "Arbiters Grounds"
    ),
    "Arbiters Grounds East Turning Room Poe": AchievementData(
        0x47700B6, "Arbiters Grounds"
    ),
    "Arbiters Grounds East Upper Turnable Chest": AchievementData(
        0x47700B7, "Arbiters Grounds"
    ),
    "Arbiters Grounds East Upper Turnable Redead Chest": AchievementData(
        0x47700B8, "Arbiters Grounds"
    ),
    "Arbiters Grounds Entrance Chest": AchievementData(0x47700B9, "Arbiters Grounds"),
    "Arbiters Grounds Ghoul Rat Room Chest": AchievementData(
        0x47700BA, "Arbiters Grounds"
    ),
    "Arbiters Grounds Hidden Wall Poe": AchievementData(0x47700BB, "Arbiters Grounds"),
    "Arbiters Grounds North Turning Room Chest": AchievementData(
        0x47700BC, "Arbiters Grounds"
    ),
    "Arbiters Grounds Spinner Room First Small Chest": AchievementData(
        0x47700BD, "Arbiters Grounds"
    ),
    "Arbiters Grounds Spinner Room Lower Central Small Chest": AchievementData(
        0x47700BE, "Arbiters Grounds"
    ),
    "Arbiters Grounds Spinner Room Lower North Chest": AchievementData(
        0x47700BF, "Arbiters Grounds"
    ),
    "Arbiters Grounds Spinner Room Second Small Chest": AchievementData(
        0x47700C0, "Arbiters Grounds"
    ),
    "Arbiters Grounds Spinner Room Stalfos Alcove Chest": AchievementData(
        0x47700C1, "Arbiters Grounds"
    ),
    "Arbiters Grounds Stallord Heart Container": AchievementData(
        0x47700C2, "Arbiters Grounds"
    ),
    "Arbiters Grounds Torch Room East Chest": AchievementData(
        0x47700C3, "Arbiters Grounds"
    ),
    "Arbiters Grounds Torch Room Poe": AchievementData(0x47700C4, "Arbiters Grounds"),
    "Arbiters Grounds Torch Room West Chest": AchievementData(
        0x47700C5, "Arbiters Grounds"
    ),
    "Arbiters Grounds West Chandelier Chest": AchievementData(
        0x47700C6, "Arbiters Grounds"
    ),
    "Arbiters Grounds West Poe": AchievementData(0x47700C7, "Arbiters Grounds"),
    "Arbiters Grounds West Small Chest Behind Block": AchievementData(
        0x47700C8, "Arbiters Grounds"
    ),
    "Arbiters Grounds West Stalfos Northeast Chest": AchievementData(
        0x47700C9, "Arbiters Grounds"
    ),
    "Arbiters Grounds West Stalfos West Chest": AchievementData(
        0x47700CA, "Arbiters Grounds"
    ),
    "Snowpeak Ruins Ball and Chain": AchievementData(0x47700CB, "Snowpeak Ruins"),
    "Snowpeak Ruins Blizzeta Heart Container": AchievementData(
        0x47700CC, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins Broken Floor Chest": AchievementData(0x47700CD, "Snowpeak Ruins"),
    "Snowpeak Ruins Chapel Chest": AchievementData(0x47700CE, "Snowpeak Ruins"),
    "Snowpeak Ruins Chest After Darkhammer": AchievementData(
        0x47700CF, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins Courtyard Central Chest": AchievementData(
        0x47700D0, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins Dungeon Reward": AchievementData(0x47700D1, "Snowpeak Ruins"),
    "Snowpeak Ruins East Courtyard Buried Chest": AchievementData(
        0x47700D2, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins East Courtyard Chest": AchievementData(0x47700D3, "Snowpeak Ruins"),
    "Snowpeak Ruins Ice Room Poe": AchievementData(0x47700D4, "Snowpeak Ruins"),
    "Snowpeak Ruins Lobby Armor Poe": AchievementData(0x47700D5, "Snowpeak Ruins"),
    "Snowpeak Ruins Lobby Chandelier Chest": AchievementData(
        0x47700D6, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins Lobby East Armor Chest": AchievementData(
        0x47700D7, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins Lobby Poe": AchievementData(0x47700D8, "Snowpeak Ruins"),
    "Snowpeak Ruins Lobby West Armor Chest": AchievementData(
        0x47700D9, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins Mansion Map": AchievementData(0x47700DA, "Snowpeak Ruins"),
    "Snowpeak Ruins Northeast Chandelier Chest": AchievementData(
        0x47700DB, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins Ordon Pumpkin Chest": AchievementData(0x47700DC, "Snowpeak Ruins"),
    "Snowpeak Ruins West Cannon Room Central Chest": AchievementData(
        0x47700DD, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins West Cannon Room Corner Chest": AchievementData(
        0x47700DE, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins West Courtyard Buried Chest": AchievementData(
        0x47700DF, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins Wooden Beam Central Chest": AchievementData(
        0x47700E0, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins Wooden Beam Chandelier Chest": AchievementData(
        0x47700E1, "Snowpeak Ruins"
    ),
    "Snowpeak Ruins Wooden Beam Northwest Chest": AchievementData(
        0x47700E2, "Snowpeak Ruins"
    ),
    "Temple of Time Armogohma Heart Container": AchievementData(
        0x47700E3, "Temple of Time"
    ),
    "Temple of Time Armos Antechamber East Chest": AchievementData(
        0x47700E4, "Temple of Time"
    ),
    "Temple of Time Armos Antechamber North Chest": AchievementData(
        0x47700E5, "Temple of Time"
    ),
    "Temple of Time Armos Antechamber Statue Chest": AchievementData(
        0x47700E6, "Temple of Time"
    ),
    "Temple of Time Big Key Chest": AchievementData(0x47700E7, "Temple of Time"),
    "Temple of Time Chest Before Darknut": AchievementData(0x47700E8, "Temple of Time"),
    "Temple of Time Darknut Chest": AchievementData(0x47700E9, "Temple of Time"),
    "Temple of Time Dungeon Reward": AchievementData(0x47700EA, "Temple of Time"),
    "Temple of Time First Staircase Armos Chest": AchievementData(
        0x47700EB, "Temple of Time"
    ),
    "Temple of Time First Staircase Gohma Gate Chest": AchievementData(
        0x47700EC, "Temple of Time"
    ),
    "Temple of Time First Staircase Window Chest": AchievementData(
        0x47700ED, "Temple of Time"
    ),
    "Temple of Time Floor Switch Puzzle Room Upper Chest": AchievementData(
        0x47700EE, "Temple of Time"
    ),
    "Temple of Time Guilloutine Chest": AchievementData(0x47700EF, "Temple of Time"),
    "Temple of Time Lobby Lantern Chest": AchievementData(0x47700F0, "Temple of Time"),
    "Temple of Time Moving Wall Beamos Room Chest": AchievementData(
        0x47700F1, "Temple of Time"
    ),
    "Temple of Time Moving Wall Dinalfos Room Chest": AchievementData(
        0x47700F2, "Temple of Time"
    ),
    "Temple of Time Poe Above Scales": AchievementData(0x47700F3, "Temple of Time"),
    "Temple of Time Poe Behind Gate": AchievementData(0x47700F4, "Temple of Time"),
    "Temple of Time Scales Gohma Chest": AchievementData(0x47700F5, "Temple of Time"),
    "Temple of Time Scales Upper Chest": AchievementData(0x47700F6, "Temple of Time"),
    "City in the Sky Aeralfos Chest": AchievementData(0x47700F7, "City in the Sky"),
    "City in the Sky Argorok Heart Container": AchievementData(
        0x47700F8, "City in the Sky"
    ),
    "City in the Sky Baba Tower Alcove Chest": AchievementData(
        0x47700F9, "City in the Sky"
    ),
    "City in the Sky Baba Tower Narrow Ledge Chest": AchievementData(
        0x47700FA, "City in the Sky"
    ),
    "City in the Sky Baba Tower Top Small Chest": AchievementData(
        0x47700FB, "City in the Sky"
    ),
    "City in the Sky Big Key Chest": AchievementData(0x47700FC, "City in the Sky"),
    "City in the Sky Central Outside Ledge Chest": AchievementData(
        0x47700FD, "City in the Sky"
    ),
    "City in the Sky Central Outside Poe Island Chest": AchievementData(
        0x47700FE, "City in the Sky"
    ),
    "City in the Sky Chest Behind North Fan": AchievementData(
        0x47700FF, "City in the Sky"
    ),
    "City in the Sky Chest Below Big Key Chest": AchievementData(
        0x4770100, "City in the Sky"
    ),
    "City in the Sky Dungeon Reward": AchievementData(0x4770101, "City in the Sky"),
    "City in the Sky East First Wing Chest After Fans": AchievementData(
        0x4770102, "City in the Sky"
    ),
    "City in the Sky East Tile Worm Small Chest": AchievementData(
        0x4770103, "City in the Sky"
    ),
    "City in the Sky East Wing After Dinalfos Alcove Chest": AchievementData(
        0x4770104, "City in the Sky"
    ),
    "City in the Sky East Wing After Dinalfos Ledge Chest": AchievementData(
        0x4770105, "City in the Sky"
    ),
    "City in the Sky East Wing Lower Level Chest": AchievementData(
        0x4770106, "City in the Sky"
    ),
    "City in the Sky Garden Island Poe": AchievementData(0x4770107, "City in the Sky"),
    "City in the Sky Poe Above Central Fan": AchievementData(
        0x4770108, "City in the Sky"
    ),
    "City in the Sky Underwater East Chest": AchievementData(
        0x4770109, "City in the Sky"
    ),
    "City in the Sky Underwater West Chest": AchievementData(
        0x477010A, "City in the Sky"
    ),
    "City in the Sky West Garden Corner Chest": AchievementData(
        0x477010B, "City in the Sky"
    ),
    "City in the Sky West Garden Ledge Chest": AchievementData(
        0x477010C, "City in the Sky"
    ),
    "City in the Sky West Garden Lone Island Chest": AchievementData(
        0x477010D, "City in the Sky"
    ),
    "City in the Sky West Garden Lower Chest": AchievementData(
        0x477010E, "City in the Sky"
    ),
    "City in the Sky West Wing Baba Balcony Chest": AchievementData(
        0x477010F, "City in the Sky"
    ),
    "City in the Sky West Wing First Chest": AchievementData(
        0x4770110, "City in the Sky"
    ),
    "City in the Sky West Wing Narrow Ledge Chest": AchievementData(
        0x4770111, "City in the Sky"
    ),
    "City in the Sky West Wing Tile Worm Chest": AchievementData(
        0x4770112, "City in the Sky"
    ),
    "Palace of Twilight Big Key Chest": AchievementData(
        0x4770113, "Palace of Twilight"
    ),
    "Palace of Twilight Central First Room Chest": AchievementData(
        0x4770114, "Palace of Twilight"
    ),
    "Palace of Twilight Central Outdoor Chest": AchievementData(
        0x4770115, "Palace of Twilight"
    ),
    "Palace of Twilight Central Tower Chest": AchievementData(
        0x4770116, "Palace of Twilight"
    ),
    "Palace of Twilight Collect Both Sols": AchievementData(
        0x4770117, "Palace of Twilight"
    ),
    "Palace of Twilight East Wing First Room East Alcove": AchievementData(
        0x4770118, "Palace of Twilight"
    ),
    "Palace of Twilight East Wing First Room North Small Chest": AchievementData(
        0x4770119, "Palace of Twilight"
    ),
    "Palace of Twilight East Wing First Room West Alcove": AchievementData(
        0x477011A, "Palace of Twilight"
    ),
    "Palace of Twilight East Wing First Room Zant Head Chest": AchievementData(
        0x477011B, "Palace of Twilight"
    ),
    "Palace of Twilight East Wing Second Room Northeast Chest": AchievementData(
        0x477011C, "Palace of Twilight"
    ),
    "Palace of Twilight East Wing Second Room Northwest Chest": AchievementData(
        0x477011D, "Palace of Twilight"
    ),
    "Palace of Twilight East Wing Second Room Southeast Chest": AchievementData(
        0x477011E, "Palace of Twilight"
    ),
    "Palace of Twilight East Wing Second Room Southwest Chest": AchievementData(
        0x477011F, "Palace of Twilight"
    ),
    "Palace of Twilight West Wing Chest Behind Wall of Darkness": AchievementData(
        0x4770120, "Palace of Twilight"
    ),
    "Palace of Twilight West Wing First Room Central Chest": AchievementData(
        0x4770121, "Palace of Twilight"
    ),
    "Palace of Twilight West Wing Second Room Central Chest": AchievementData(
        0x4770122, "Palace of Twilight"
    ),
    "Palace of Twilight West Wing Second Room Lower South Chest": AchievementData(
        0x4770123, "Palace of Twilight"
    ),
    "Palace of Twilight West Wing Second Room Southeast Chest": AchievementData(
        0x4770124, "Palace of Twilight"
    ),
    "Palace of Twilight Zant Heart Container": AchievementData(
        0x4770125, "Palace of Twilight"
    ),
    "Hyrule Castle Big Key Chest": AchievementData(0x4770126, "Hyrule Castle"),
    "Hyrule Castle East Wing Balcony Chest": AchievementData(
        0x4770127, "Hyrule Castle"
    ),
    "Hyrule Castle East Wing Boomerang Puzzle Chest": AchievementData(
        0x4770128, "Hyrule Castle"
    ),
    "Hyrule Castle Graveyard Grave Switch Room Back Left Chest": AchievementData(
        0x4770129, "Hyrule Castle"
    ),
    "Hyrule Castle Graveyard Grave Switch Room Front Left Chest": AchievementData(
        0x477012A, "Hyrule Castle"
    ),
    "Hyrule Castle Graveyard Grave Switch Room Right Chest": AchievementData(
        0x477012B, "Hyrule Castle"
    ),
    "Hyrule Castle Graveyard Owl Statue Chest": AchievementData(
        0x477012C, "Hyrule Castle"
    ),
    "Hyrule Castle King Bulblin Key": AchievementData(0x477012D, "Hyrule Castle"),
    "Hyrule Castle Lantern Staircase Chest": AchievementData(
        0x477012E, "Hyrule Castle"
    ),
    "Hyrule Castle Main Hall Northeast Chest": AchievementData(
        0x477012F, "Hyrule Castle"
    ),
    "Hyrule Castle Main Hall Northwest Chest": AchievementData(
        0x4770130, "Hyrule Castle"
    ),
    "Hyrule Castle Main Hall Southwest Chest": AchievementData(
        0x4770131, "Hyrule Castle"
    ),
    "Hyrule Castle Southeast Balcony Tower Chest": AchievementData(
        0x4770132, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Eighth Small Chest": AchievementData(
        0x4770133, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Fifth Chest": AchievementData(
        0x4770134, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Fifth Small Chest": AchievementData(
        0x4770135, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room First Chest": AchievementData(
        0x4770136, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room First Small Chest": AchievementData(
        0x4770137, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Fourth Chest": AchievementData(
        0x4770138, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Fourth Small Chest": AchievementData(
        0x4770139, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Second Chest": AchievementData(
        0x477013A, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Second Small Chest": AchievementData(
        0x477013B, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Seventh Small Chest": AchievementData(
        0x477013C, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Sixth Small Chest": AchievementData(
        0x477013D, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Third Chest": AchievementData(
        0x477013E, "Hyrule Castle"
    ),
    "Hyrule Castle Treasure Room Third Small Chest": AchievementData(
        0x477013F, "Hyrule Castle"
    ),
    "Hyrule Castle West Courtyard Central Small Chest": AchievementData(
        0x4770140, "Hyrule Castle"
    ),
    "Hyrule Castle West Courtyard North Small Chest": AchievementData(
        0x4770141, "Hyrule Castle"
    ),
    "Ordon Shield": AchievementData(0x4770142, "Ordon Village"),
    "Ordon Sword": AchievementData(0x4770143, "Ordon Village"),
    "Faron Field Tree Heart Piece": AchievementData(
        0x4770144, "Hyrule Field - Faron Field"
    ),
    "Cats Hide and Seek Minigame": AchievementData(0x4770145, "Hidden Village"),
    "Kakariko Gorge Spire Heart Piece": AchievementData(
        0x4770146, "Hyrule Field - Kakariko Gorge"
    ),
    "Kakariko Village Bomb Rock Spire Heart Piece": AchievementData(
        0x4770147, "Kakariko Village"
    ),
    "Fishing Hole Heart Piece": AchievementData(0x4770148, "Fishing Hole"),
    "Bulblin Camp Roasted Boar": AchievementData(0x4770149, "Bulblin Camp"),
    "Bulblin Guard Key": AchievementData(0x477014A, "Bulblin Camp"),
    "Herding Goats Reward": AchievementData(0x477014B, "Ordon Ranch"),
    "Ordon Cat Rescue": AchievementData(0x477014C, "Ordon Village"),
    "Uli Cradle Delivery": AchievementData(0x477014D, "Ordon Village"),
    "Wrestling With Bo": AchievementData(0x477014E, "Ordon Village"),
    "Coro Bottle": AchievementData(0x4770150, "South Faron Woods"),
    "Barnes Bomb Bag": AchievementData(0x4770151, "Kakariko Village"),
    "Gift From Ralis": AchievementData(0x4770153, "Kakariko Graveyard"),
    "Goron Springwater Rush": AchievementData(0x4770154, "Hyrule Field - Eldin Field"),
    "Ilia Charm": AchievementData(0x4770155, "Hidden Village"),
    "Ilia Memory Reward": AchievementData(0x4770156, "Kakariko Village"),
    "Renados Letter": AchievementData(0x4770157, "Kakariko Village"),
    "Rutelas Blessing": AchievementData(0x4770158, "Kakariko Graveyard"),
    "Skybook From Impaz": AchievementData(0x4770159, "Hidden Village"),
    "Talo Sharpshooting": AchievementData(0x477015A, "Kakariko Village"),
    "Agitha Female Ant Reward": AchievementData(0x477015B, "Castle Town"),
    "Agitha Female Beetle Reward": AchievementData(0x477015C, "Castle Town"),
    "Agitha Female Butterfly Reward": AchievementData(0x477015D, "Castle Town"),
    "Agitha Female Dayfly Reward": AchievementData(0x477015E, "Castle Town"),
    "Agitha Female Dragonfly Reward": AchievementData(0x4770160, "Castle Town"),
    "Agitha Female Grasshopper Reward": AchievementData(0x4770161, "Castle Town"),
    "Agitha Female Ladybug Reward": AchievementData(0x4770162, "Castle Town"),
    "Agitha Female Mantis Reward": AchievementData(0x4770163, "Castle Town"),
    "Agitha Female Phasmid Reward": AchievementData(0x4770164, "Castle Town"),
    "Agitha Female Pill Bug Reward": AchievementData(0x4770165, "Castle Town"),
    "Agitha Female Snail Reward": AchievementData(0x4770166, "Castle Town"),
    "Agitha Female Stag Beetle Reward": AchievementData(0x4770167, "Castle Town"),
    "Agitha Male Ant Reward": AchievementData(0x4770168, "Castle Town"),
    "Agitha Male Beetle Reward": AchievementData(0x4770169, "Castle Town"),
    "Agitha Male Butterfly Reward": AchievementData(0x477016A, "Castle Town"),
    "Agitha Male Dayfly Reward": AchievementData(0x477016B, "Castle Town"),
    "Agitha Male Dragonfly Reward": AchievementData(0x477016C, "Castle Town"),
    "Agitha Male Grasshopper Reward": AchievementData(0x477016D, "Castle Town"),
    "Agitha Male Ladybug Reward": AchievementData(0x477016E, "Castle Town"),
    "Agitha Male Mantis Reward": AchievementData(0x477016F, "Castle Town"),
    "Agitha Male Phasmid Reward": AchievementData(0x4770170, "Castle Town"),
    "Agitha Male Pill Bug Reward": AchievementData(0x4770171, "Castle Town"),
    "Agitha Male Snail Reward": AchievementData(0x4770172, "Castle Town"),
    "Agitha Male Stag Beetle Reward": AchievementData(0x4770173, "Castle Town"),
    "Auru Gift to Fyer": AchievementData(0x4770174, "Lake Hylia"),
    "Charlo Donation Blessing": AchievementData(0x4770175, "Castle Town"),
    "Iza Helping Hand": AchievementData(0x4770176, "Upper Zoras River"),
    "Iza Raging Rapids Minigame": AchievementData(0x4770177, "Upper Zoras River"),
    "Jovani 20 Poe Soul Reward": AchievementData(0x4770178, "Castle Town"),
    "Jovani 60 Poe Soul Reward": AchievementData(0x4770179, "Castle Town"),
    "Plumm Fruit Balloon Minigame": AchievementData(0x477017A, "Upper Zoras River"),
    "STAR Prize 1": AchievementData(0x477017B, "Castle Town"),
    "STAR Prize 2": AchievementData(0x477017C, "Castle Town"),
    "Telma Invoice": AchievementData(0x477017D, "Castle Town"),
    "Zoras Domain Underwater Goron": AchievementData(0x477017E, "Zoras Domain"),
    "Ashei Sketch": AchievementData(0x477017F, "Snowpeak"),
    "Snowboard Racing Prize": AchievementData(0x4770180, "Snowpeak"),
    "Cave of Ordeals Great Fairy Reward": AchievementData(0x4770181, "Cave of Ordeals"),
    "Faron Field Female Beetle": AchievementData(
        0x4770182, "Hyrule Field - Faron Field"
    ),
    "Faron Field Male Beetle": AchievementData(0x4770183, "Hyrule Field - Faron Field"),
    "Sacred Grove Female Snail": AchievementData(0x4770184, "Sacred Grove - Past"),
    "Sacred Grove Male Snail": AchievementData(
        0x4770185, "Sacred Grove - Master Sword Area"
    ),
    "Bridge of Eldin Female Phasmid": AchievementData(
        0x4770186, "Hyrule Field - Eldin Field"
    ),
    "Bridge of Eldin Male Phasmid": AchievementData(
        0x4770187, "Hyrule Field - Eldin Field"
    ),
    "Eldin Field Female Grasshopper": AchievementData(
        0x4770188, "Hyrule Field - Eldin Field"
    ),
    "Eldin Field Male Grasshopper": AchievementData(
        0x4770189, "Hyrule Field - Eldin Field"
    ),
    "Kakariko Gorge Female Pill Bug": AchievementData(
        0x477018A, "Hyrule Field - Kakariko Gorge"
    ),
    "Kakariko Gorge Male Pill Bug": AchievementData(
        0x477018B, "Hyrule Field - Kakariko Gorge"
    ),
    "Kakariko Graveyard Male Ant": AchievementData(0x477018C, "Kakariko Graveyard"),
    "Kakariko Village Female Ant": AchievementData(0x477018D, "Kakariko Village"),
    "Lake Hylia Bridge Female Mantis": AchievementData(
        0x477018E, "Hyrule Field - Bridge of Hylia"
    ),
    "Lake Hylia Bridge Male Mantis": AchievementData(
        0x477018F, "Hyrule Field - Bridge of Hylia"
    ),
    "Lanayru Field Female Stag Beetle": AchievementData(
        0x4770190, "Hyrule Field - Lanayru Field"
    ),
    "Lanayru Field Male Stag Beetle": AchievementData(
        0x4770191, "Hyrule Field - Lanayru Field"
    ),
    "Outside South Castle Town Female Ladybug": AchievementData(
        0x4770192, "Hyrule Field - Outside South Castle Town"
    ),
    "Outside South Castle Town Male Ladybug": AchievementData(
        0x4770193, "Hyrule Field - Outside South Castle Town"
    ),
    "Upper Zoras River Female Dragonfly": AchievementData(
        0x4770194, "Upper Zoras River"
    ),
    "West Hyrule Field Female Butterfly": AchievementData(
        0x4770195, "Hyrule Field - Outside West Castle Town"
    ),
    "West Hyrule Field Male Butterfly": AchievementData(
        0x4770196, "Hyrule Field - Outside West Castle Town"
    ),
    "Zoras Domain Male Dragonfly": AchievementData(0x4770197, "Zoras Domain"),
    "Gerudo Desert Female Dayfly": AchievementData(0x4770198, "Gerudo Desert"),
    "Gerudo Desert Male Dayfly": AchievementData(0x4770198, "Gerudo Desert"),
    "Faron Mist Poe": AchievementData(0x4770199, "Faron Mist Area"),
    "Lost Woods Waterfall Poe": AchievementData(0x477019A, "Lost Woods"),
    "Sacred Grove Temple of Time Owl Statue Poe": AchievementData(
        0x477019B, "Sacred Grove - Past"
    ),
    "Lost Woods Boulder Poe": AchievementData(0x477019C, "Lost Woods"),
    "Sacred Grove Master Sword Poe": AchievementData(
        0x477019D, "Sacred Grove - Master Sword Area"
    ),
    "Faron Field Poe": AchievementData(0x477019E, "Hyrule Field - Faron Field"),
    "Kakariko Gorge Poe": AchievementData(0x477019F, "Hyrule Field - Kakariko Gorge"),
    "Eldin Lantern Cave Poe": AchievementData(0x47701A0, "Eldin Lantern Cave"),
    "Kakariko Graveyard Open Poe": AchievementData(0x47701A1, "Kakariko Graveyard"),
    "Kakariko Graveyard Grave Poe": AchievementData(0x47701A2, "Kakariko Graveyard"),
    "Kakariko Village Bomb Shop Poe": AchievementData(0x47701A3, "Kakariko Village"),
    "Kakariko Village Watchtower Poe": AchievementData(0x47701A4, "Kakariko Village"),
    "Death Mountain Trail Poe": AchievementData(0x47701A5, "Death Mountain"),
    "Hidden Village Poe": AchievementData(0x47701A6, "Hidden Village"),
    "Upper Zoras River Poe": AchievementData(0x47701A7, "Upper Zoras River"),
    "Zoras Domain Mother and Child Isle Poe": AchievementData(
        0x47701A8, "Zoras Domain"
    ),
    "Zoras Domain Waterfall Poe": AchievementData(0x47701A8, "Zoras Domain"),
    "Snowpeak Blizzard Poe": AchievementData(0x47701A9, "Snowpeak"),
    "Snowpeak Above Freezard Grotto Poe": AchievementData(0x47701AA, "Snowpeak"),
    "Snowpeak Poe Among Trees": AchievementData(0x47701AB, "Snowpeak"),
    "Snowpeak Icy Summit Poe": AchievementData(0x47701AC, "Snowpeak"),
    "Snowpeak Cave Ice Poe": AchievementData(0x47701AD, "Snowpeak"),
    "Lanayru Field Bridge Poe": AchievementData(
        0x47701AE, "Hyrule Field - Lanayru Field"
    ),
    "Lanayru Field Poe Grotto Left Poe": AchievementData(
        0x47701AE, "Hyrule Field - Lanayru Field"
    ),
    "Lanayru Field Poe Grotto Right Poe": AchievementData(
        0x47701AE, "Hyrule Field - Lanayru Field"
    ),
    "Outside South Castle Town Poe": AchievementData(
        0x47701AF, "Hyrule Field - Outside South Castle Town"
    ),
    "East Castle Town Bridge Poe": AchievementData(
        0x47701B0, "Hyrule Field - Outside East Castle Town"
    ),
    "Jovani House Poe": AchievementData(0x47701B1, "Castle Town"),
    "Hyrule Field Ampitheater Poe": AchievementData(
        0x47701B2,
        "Hyrule Field - Outside West Castle Town",
    ),
    "Flight By Fowl Ledge Poe": AchievementData(0x47701B3, "Lake Hylia"),
    "Isle of Riches Poe": AchievementData(0x47701B4, "Lake Hylia"),
    "Lake Hylia Dock Poe": AchievementData(0x47701B5, "Lake Hylia"),
    "Lake Hylia Tower Poe": AchievementData(0x47701B6, "Lake Hylia"),
    "Lake Hylia Alcove Poe": AchievementData(0x47701B7, "Lake Hylia"),
    "Lake Lantern Cave First Poe": AchievementData(0x47701B8, "Lake Lantern Cave"),
    "Lake Lantern Cave Second Poe": AchievementData(0x47701B9, "Lake Lantern Cave"),
    "Lake Lantern Cave Final Poe": AchievementData(0x47701BA, "Lake Lantern Cave"),
    "Lake Hylia Bridge Cliff Poe": AchievementData(
        0x47701BB, "Hyrule Field - Lake Hylia Bridge"
    ),
    "Gerudo Desert East Poe": AchievementData(0x47701BC, "Gerudo Desert"),
    "Gerudo Desert North Peahat Poe": AchievementData(0x47701BD, "Gerudo Desert"),
    "Gerudo Desert Rock Grotto First Poe": AchievementData(0x47701BE, "Gerudo Desert"),
    "Gerudo Desert Rock Grotto Second Poe": AchievementData(0x47701BF, "Gerudo Desert"),
    "Outside Bulblin Camp Poe": AchievementData(0x47701C0, "Gerudo Desert"),
    "Bulblin Camp Poe": AchievementData(0x47701C1, "Bulblin Camp"),
    "Outside Arbiters Grounds Poe": AchievementData(0x47701C2, "Bulblin Camp"),
    "Gerudo Desert Poe Above Cave of Ordeals": AchievementData(
        0x47701C3, "Gerudo Desert"
    ),
    "Cave of Ordeals Floor 17 Poe": AchievementData(0x47701C4, "Cave of Ordeals"),
    "Cave of Ordeals Floor 33 Poe": AchievementData(0x47701C5, "Cave of Ordeals"),
    "Cave of Ordeals Floor 44 Poe": AchievementData(0x47701C5, "Cave of Ordeals"),
    "Faron Woods Owl Statue Sky Character": AchievementData(
        0x47701C6, "South Faron Woods"
    ),
    "Kakariko Gorge Owl Statue Sky Character": AchievementData(
        0x47701C7, "Hyrule Field - Kakariko Gorge"
    ),
    "Bridge of Eldin Owl Statue Sky Character": AchievementData(
        0x47701C8, "Hyrule Field - Eldin Field"
    ),
    "Hyrule Field Ampitheater Owl Statue Sky Character": AchievementData(
        0x47701C9, "Hyrule Field - Outside West Castle Town"
    ),
    "Lake Hylia Bridge Owl Statue Sky Character": AchievementData(
        0x47701CA, "Hyrule Field - Bridge of Hylia"
    ),
    "Gerudo Desert Owl Statue Sky Character": AchievementData(
        0x47701CB, "Gerudo Desert"
    ),
    "Sera Shop Slingshot": AchievementData(0x47701CC, "Ordon Village"),
    "Kakariko Village Malo Mart Hawkeye": AchievementData(
        0x47701CD, "Kakariko Village"
    ),
    "Kakariko Village Malo Mart Hylian Shield": AchievementData(
        0x47701CE, "Kakariko Village"
    ),
    "Kakariko Village Malo Mart Red Potion": AchievementData(
        0x47701CF, "Kakariko Village"
    ),
    "Kakariko Village Malo Mart Wooden Shield": AchievementData(
        0x47701D0, "Kakariko Village"
    ),
    "Castle Town Malo Mart Magic Armor": AchievementData(0x47701D1, "Castle Town"),
    "Ordon Spring Golden Wolf": AchievementData(0x47701D2, "Ordon Spring"),
    "Faron Woods Golden Wolf": AchievementData(0x47701D3, "North Faron Woods"),
    "Kakariko Graveyard Golden Wolf": AchievementData(0x47701D4, "Kakariko Graveyard"),
    "North Castle Town Golden Wolf": AchievementData(0x47701D5, "Castle Town"),
    "Outside South Castle Town Golden Wolf": AchievementData(
        0x47701D6, "Hyrule Field - Outside South Castle Town"
    ),
    "West Hyrule Field Golden Wolf": AchievementData(
        0x47701D7, "Hyrule Field - Outside West Castle Town"
    ),
    "Gerudo Desert Golden Wolf": AchievementData(0x47701D8, "Gerudo Desert"),
    "Eldin Field Water Bomb Fish Grotto Chest": AchievementData(
        0x47701D9, "Hyrule Field - Eldin Field"
    ),
    "Mirror Chamber Mirror Shard": AchievementData(0x47701DA, "Arbiters Grounds"),
}

lookup_id_to_name: Dict[int, str] = {
    loc_data.id: loc_name
    for loc_name, loc_data in achievement_table.items()
    if loc_data.id
}
