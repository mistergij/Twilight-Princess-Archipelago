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
}
