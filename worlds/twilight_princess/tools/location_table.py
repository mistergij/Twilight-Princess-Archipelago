"""Table of locations that are available"""
import dataclasses


@dataclasses.dataclass
class Location:
    """Class that defines locations for checks"""

    name: str
    address: int
    flag: int
    region: bool
    displacement: int


location_table: list[Location] = [
    Location("Agitha Female Ant Reward", 0x804069E4, 0x80, False, -1),
    Location("Agitha Female Beetle Reward", 0x804069E1, 0x8, False, -1),
    Location("Agitha Female Butterfly Reward", 0x804069E1, 0x2, False, -1),
    Location("Agitha Female Dayfly Reward", 0x804069E4, 0x20, False, -1),
    Location("Agitha Female Dragonfly Reward", 0x804069E3, 0x2, False, -1),
    Location("Agitha Female Grasshopper Reward", 0x804069E2, 0x20, False, -1),
    Location("Agitha Female Ladybug Reward", 0x804069E3, 0x20, False, -1),
    Location("Agitha Female Mantis Reward", 0x804069E3, 0x80, False, -1),
    Location("Agitha Female Phasmid Reward", 0x804069E2, 0x8, False, -1),
    Location("Agitha Female Pill Bug Reward", 0x804069E2, 0x2, False, -1),
    Location("Agitha Female Snail Reward", 0x804069E3, 0x8, False, -1),
    Location("Agitha Female Stag Beetle Reward", 0x804069E2, 0x80, False, -1),
    Location("Agitha Male Ant Reward", 0x804069E3, 0x1, False, -1),
    Location("Agitha Male Beetle Reward", 0x804069E1, 0x10, False, -1),
    Location("Agitha Male Butterfly Reward", 0x804069E1, 0x4, False, -1),
    Location("Agitha Male Dayfly Reward", 0x804069E4, 0x40, False, -1),
    Location("Agitha Male Dragonfly Reward", 0x804069E3, 0x4, False, -1),
    Location("Agitha Male Grasshopper Reward", 0x804069E2, 0x40, False, -1),
    Location("Agitha Male Ladybug Reward", 0x804069E3, 0x40, False, -1),
    Location("Agitha Male Mantis Reward", 0x804069E2, 0x1, False, -1),
    Location("Agitha Male Phasmid Reward", 0x804069E2, 0x10, False, -1),
    Location("Agitha Male Pill Bug Reward", 0x804069E2, 0x4, False, -1),
    Location("Agitha Male Snail Reward", 0x804069E3, 0x10, False, -1),
    Location("Agitha Male Stag Beetle Reward", 0x804069E1, 0x1, False, -1),
    Location("Ariters Grounds Big Key Chest", 0x80406610, 0x10, True, 0x1),
    Location("Arbiters Grounds Death Sword Chest", 0x80406610, 0x8, True, 0x2),
    Location(
        "Arbiters Grounds East Lower Turnable Redead Chest",
        0x80406610,
        0x40,
        True,
        0x3,
    ),
    Location("Arbiters Grounds East Turning Room Poe", 0x80406610, 0x10, True, 0xA),
    Location("Arbiters Grounds East Upper Turnable Chest", 0x80406610, 0x10, True, 0x3),
    Location(
        "Arbiters Grounds East Upper Turnable Redead Chest", 0x80406610, 0x20, True, 0x3
    ),
    Location("Arbiters Grounds Entrance Chest", 0x80406610, 0x80, True, 0x0),
    Location("Arbiters Grounds Ghoul Rat Room Chest", 0x80406610, 0x20, True, 0x1),
    Location("Arbiters Grounds Hidden Wall Poe", 0x80406610, 0x4, True, 0x11),
    Location("Arbiters Grounds North Turning Room Chest", 0x80406610, 0x1, True, 0x0),
    Location(
        "Arbiters Grounds Spinner Room First Small Chest", 0x80406610, 0x10, True, 0x0
    ),
    Location(
        "Arbiters Grounds Spinner Room Lower Central Small Chest",
        0x80406610,
        0x20,
        True,
        0x0,
    ),
    Location(
        "Arbiters Grounds Spinner Room Lower North Chest", 0x80406610, 0x40, True, 0x0
    ),
    Location(
        "Arbiters Grounds Spinner Room Second Small Chest", 0x80406610, 0x8, True, 0x0
    ),
    Location(
        "Arbiters Grounds Spinner Room Stalfos Alcove Chest", 0x80406610, 0x4, True, 0x0
    ),
    Location("Arbiters Grounds Stallord Heart Container", 0x80406610, 0x10, True, 0x1D),
    Location("Arbuters Grounds Torch Room East Chest", 0x80406610, 0x8, True, 0x1),
    Location("Arbiters Grounds Torch Room Poe", 0x80406610, 0x40, True, 0x8),
    Location("Arbiters Grounds Torch Room West Chest", 0x80406610, 0x4, True, 0x1),
    Location("Arbiters Grounds West Chandelier Chest", 0x80406610, 0x8, True, 0x3),
    Location("Arbiters Grounds West Poe", 0x80406610, 0x2, True, 0xF),
    Location(
        "Arbiters Grounds West Small Chest Behind Block", 0x80406610, 0x2, True, 0x0
    ),
    Location(
        "Arbiters Grounds West Stalfos Northeast Cave", 0x80406610, 0x1, True, 0x1
    ),
    Location("Arbiters Grounds West Stalfos West Chest", 0x80406610, 0x2, True, 0x1),
    Location("Ashei Sketch", -1, -1, -1, -1),
    Location("Auru Gift to Fyer", -1, -1, -1, -1),
    Location("Barnes Bomb Bag", 0x804069B9, 0x8, False, -1),
    Location("Bridge of Eldin Female Phasmid", -1, -1, -1, -1),
    Location("Bridge of Elldin Male Phasmid", -1, -1, -1, -1),
    Location("Bridge of Eldin Owl Statue Chest", -1, -1, -1, -1),
    Location("Bridge of Eldin Owl Statue Sky Character", -1, -1, -1, -1),
    Location("Bulblin Camp First Chest Under Tower At Entrance", -1, -1, -1, -1),
    Location("Bulblin Camp Poe", -1, -1, -1, -1),
    Location("Bulblin Camp Roasted Boar", -1, -1, -1, -1),
    Location("Bulblin Camp Small Chest in Back of Camp", -1, -1, -1, -1),
    Location("Bulblin Guard Key", -1, -1, -1, -1),
    Location("Castle Town Malo Mart Magic Armor", -1, -1, -1, -1),
    Location("Cats Hide and Seek Minigame", -1, -1, -1, -1),
    Location("Cave of Ordeals Floor 17 Poe", -1, -1, -1, -1),
    Location("Cave of Ordeals Floor 33 Poe", -1, -1, -1, -1),
    Location("Cave of Ordeals Floor 44 Poe", -1, -1, -1, -1),
    Location("Cave of Ordeals Great Fairy Rewards", -1, -1, -1, -1),
    Location("Charlo Donation Blessing", -1, -1, -1, -1),
    Location("City in the Sky Aeralfos Chest", 0x80406670, 0x1, True, 0x3),
    Location("City in the Sky Argorok Heart Container", 0x80406670, 0x10, True, 0x1D),
    Location("City in the Sky Baba Tower Alcove Chest", 0x80406670, 0x40, True, 0x3),
    Location(
        "City in the Sky Baba Tower Narrow Ledge Chest", 0x80406670, 0x80, True, 0x1
    ),
    Location("City in the Sky Baba Tower Top Small Chest", 0x80406670, 0x80, True, 0x3),
    Location("City in the Sky Big Key Chest", 0x80406670, 0x20, True, 0x2),
    Location("City in the Sky Central Outside Ledge Chest", 0x80406670, 0x1, True, 0x0),
    Location(
        "City in the Sky Central Outside Poe Island Chest", 0x80406670, 0x10, True, 0x2
    ),
    Location("City in the Sky Chest Behind North Fan", 0x80406670, 0x2, True, 0x1),
    Location("City in the Sky Chest Below Big Key Chest", 0x80406670, 0x40, True, 0x2),
    Location("City in the Sky Dungeon Reward", 0x80406670, 0x8, True, 0x1D),
    Location(
        "City in the Sky East First Wing Chest After Fans", 0x80406670, 0x4, True, 0x3
    ),
    Location("City in the Sky East Tile Worm Small Chest", 0x80406670, 0x8, True, 0x1),
    Location(
        "City in the Sky East Wing After Dinalfos Alcove Chest",
        0x80406670,
        0x4,
        True,
        0x1,
    ),
    Location(
        "City in the Sky East Wing after Dinalfos Ledge Chest",
        0x80406670,
        0x4,
        True,
        0x0,
    ),
    Location(
        "City in the Sky East Wing Lower Level Chest", 0x80406670, 0x10, True, 0x3
    ),
    Location("City in the Sky Garden Island Poe", 0x80406670, 0x10, True, 0x11),
    Location("City in the Sky Poe Above Central Fan", 0x80406670, 0x20, True, 0x11),
    Location("City in the Sky Underwater East Chest", 0x80406670, 0x8, True, 0x0),
    Location("City in the Sky Underwater West Chest", 0x80406670, 0x8, True, 0x3),
    Location("City in the Sky West Garden Corner Chest", 0x80406670, 0x80, True, 0x2),
    Location("City in the Sky West Garden Ledge Chest", 0x80406670, 0x2, True, 0x2),
    Location(
        "City in the Sky West Garden Lone Island Chest", 0x80406670, 0x2, True, 0x0
    ),
    Location("City in the Sky West Garden Lower Chest", 0x80406670, 0x8, True, 0x2),
    Location(
        "City in the Sky West Wing Baba Balcony Chest", 0x80406670, 0x20, True, 0x1
    ),
    Location("City in the Sky West Wing First Chest", 0x80406670, 0x20, True, 0x3),
    Location(
        "City in the Sky West Wing Narrow Ledge Chest", 0x80406670, 0x10, True, 0x1
    ),
    Location("City in the Sky West Wing Tile Worm Chest", 0x80406670, 0x40, True, 0x3),
    Location("Coro Bottle", -1, -1, -1, -1),
    Location("Death Mountain Alcove Chest", -1, -1, -1, -1),
    Location("Death Mountain Trail Poe", -1, -1, -1, -1),
    Location("Doctors Office Balcony Chest", -1, -1, -1, -1),
    Location("East Castle Town Bridge Poe", -1, -1, -1, -1),
    Location("Eldin Field Bomb Rock Chest", -1, -1, -1, -1),
    Location("Eldin Field Bomskit Grotto Lantern Chest", -1, -1, -1, -1),
    Location("Eldin Field Bomskit Grotto Left Chest", -1, -1, -1, -1),
    Location("Eldin Field Female Grasshopper", -1, -1, -1, -1),
    Location("Eldin Field Male Grasshopper", -1, -1, -1, -1),
    Location("Eldin Field Stalfos Grotto Left Small Chest", -1, -1, -1, -1),
    Location("Eldin Field Stalfos Grotto Right Small Chest", -1, -1, -1, -1),
    Location("Eldin Field Stalfos Grotto Stalfos Chest", -1, -1, -1, -1),
    Location("Eldin Field Water Bomb Fish Grotto Chest", -1, -1, -1, -1),
    Location("Eldin Lantern Cave First Chest", -1, -1, -1, -1),
    Location("Eldin Lantern Cave Lantern Chest", -1, -1, -1, -1),
    Location("Eldin Lantern Cave Poe", -1, -1, -1, -1),
    Location("Eldin Lantern Cave Second Chest", -1, -1, -1, -1),
    Location("Eldin Spring Underwater Chest", -1, -1, -1, -1),
    Location("Eldin Stockcave Lantern Chest", -1, -1, -1, -1),
    Location("Eldin Stockcave Lowest Chest", -1, -1, -1, -1),
    Location("Eldin Stockcave Upper Chest", -1, -1, -1, -1),
    Location("Faron Field Bridge Chest", -1, -1, -1, -1),
    Location("Faron Field Corner Grotto Left Chest", -1, -1, -1, -1),
    Location("Faron Field Corner Grotto Rear Chest", -1, -1, -1, -1),
    Location("Faron Field Corner Grotto Right Chest", -1, -1, -1, -1),
    Location("Faron Field Female Beetle", -1, -1, -1, -1),
    Location("Faron Field Male Beetle", -1, -1, -1, -1),
    Location("Faron Field Poe", -1, -1, -1, -1),
    Location("Faron Field Tree Heart Piece", -1, -1, -1, -1),
    Location("Faron Mist Cave Lantern Chest", -1, -1, -1, -1),
    Location("Faron Mist Cave Open Chest", -1, -1, -1, -1),
    Location("Faron Mist North Chest", -1, -1, -1, -1),
    Location("Faron Mist Poe", -1, -1, -1, -1),
    Location("Faron Mist South Chest", -1, -1, -1, -1),
    Location("Faron Mist Stump Chest", -1, -1, -1, -1),
    Location("Faron Woods Golden Wolf", -1, -1, -1, -1),
    Location("Faron Woods Owl Statue Chest", -1, -1, -1, -1),
    Location("Faron Woods Owl Statue Sky Character", -1, -1, -1, -1),
    Location("Fishing Hole Bottle", -1, -1, -1, -1),
    Location("Fishing Hole Heart Piece", -1, -1, -1, -1),
    Location("Flight By Fowl Fifth Platform Chest", -1, -1, -1, -1),
    Location("Flight By Fowl Fourth Platform Chest", -1, -1, -1, -1),
    Location("Flight By Fowl Ledge Poe", -1, -1, -1, -1),
    Location("Flight By Fowl Second Platform Chest", -1, -1, -1, -1),
    Location("Flight By Fowl Third Platform Chest", -1, -1, -1, -1),
    Location("Flight By Fowl Top Platform Reward", -1, -1, -1, -1),
    Location("Forest Temple Big Baba Key", 0x804065B0, 0x40, True, 0x3),
    Location("Forest Temple Big Key Chest", 0x804065B0, 0x40, True, 0x7),
    Location("Forest Temple Central Chest Behind Stairs", 0x804065B0, 0x20, True, 0x7),
    Location(
        "Forest Temple Central Chest Hanging From Web", 0x804065B0, 0x10, True, 0x1
    ),
    Location("Forest Temple Central North Chest", 0x804065B0, 0x80, True, 0x7),
    Location("Forest Temple Diababa Heart Container", 0x804065B0, 0x10, True, 0x1D),
    Location("Forest Temple Dungeon Reward", 0x804065B0, 0x8, True, 0x1D),
    Location("Forest Temple East Tile Worm Chest", 0x804065B0, 0x2, True, 0x3),
    Location("Forest Temple East Water Cave Chest", 0x804065B0, 0x4, True, 0x0),
    Location("Forest Temple Entrance Vines Chest", 0x804065B0, 0x80, True, 0x3),
    Location("Forest Temple Gale Boomerang", 0x804065B0, 0x80, True, 0x1D),
    Location("Forest Temple North Deku Like Chest", 0x804065B0, 0x4, True, 0x3),
    Location(
        "Forest Temple Second Monkey Under Bridge Chest", 0x804065B0, 0x2, True, 0x2
    ),
    Location("Forest Temple Totem Pole Chest", 0x804065B0, 0x2, True, 0x0),
    Location("Forest Temple West Deku Like Chest", 0x804065B0, 0x80, True, 0x0),
    Location(
        "Forest Temple West Tile Worm Chest Behind Stairs", 0x804065B0, 0x8, True, 0x1
    ),
    Location(
        "Forest Temple West Tile Worm Room Vines Chest", 0x804065B0, 0x1, True, 0x0
    ),
    Location("Forest Temple Windless Bridge Chest", 0x804065B0, 0x10, True, 0x3),
    Location("Gerudo Desert Campfire East Chest", -1, -1, -1, -1),
    Location("Gerudo Desert Campfire North Chest", -1, -1, -1, -1),
    Location("Gerudo Desert Campfire West Chest", -1, -1, -1, -1),
    Location("Gerudo Desert East Canyon Chest", -1, -1, -1, -1),
    Location("Gerudo Desert East Poe", -1, -1, -1, -1),
    Location("Gerudo Desert Female Dayfly", -1, -1, -1, -1),
    Location("Gerudo Desert Golden Wolf", -1, -1, -1, -1),
    Location("Gerudo Desert Lone Small Chest", -1, -1, -1, -1),
    Location("Gerudo Desert Male Dayfly", -1, -1, -1, -1),
    Location("Gerudo Desert North Peahat Poe", -1, -1, -1, -1),
    Location("Gerudo Desert North Small Chest Before Bulblin Camp", -1, -1, -1, -1),
    Location("Gerudo Desert Northeast Chest Behind Gates", -1, -1, -1, -1),
    Location("Gerudo Desert Northwest Chest Behind Gates", -1, -1, -1, -1),
    Location("Gerudo Desert Owl Statue Chest", -1, -1, -1, -1),
    Location("Gerudo Desert Owl Statue Sky Character", -1, -1, -1, -1),
    Location("Gerudo Desert Peahat Ledge Chest", -1, -1, -1, -1),
    Location("Gerudo Desert Poe Above Cave of Ordeals", -1, -1, -1, -1),
    Location("Gerudo Desert Rock Grotto First Poe", -1, -1, -1, -1),
    Location("Gerudo Desert Rock Grotto Lantern Chest", -1, -1, -1, -1),
    Location("Gerudo Desert Rock Grotto Second Poe", -1, -1, -1, -1),
    Location("Gerudo Desert Skulltula Grotto Chest", -1, -1, -1, -1),
    Location("Gerudo Desert South Chest Behind Wooden Gates", -1, -1, -1, -1),
    Location("Gerudo Desert West Canyon Chest", -1, -1, -1, -1),
    Location("Gift From Ralis", -1, -1, -1, -1),
    Location(
        "Goron Mines After Crystal Switch Room Magnet Wall Chest",
        0x804065D0,
        0x2,
        True,
        0x2,
    ),
    Location("Goron Mines Beamos Room Chest", 0x804065D0, 0x10, True, 0x2),
    Location("Goron Mines Chest Before Dangoro", 0x804065D0, 0x20, True, 0x2),
    Location(
        "Goron Mines Crystal Switch Room Small Chest", 0x804065D0, 0x10, True, 0x0
    ),
    Location(
        "Goron Mines Crystal Switch Room Underwater Chest", 0x804065D0, 0x1, True, 0x1
    ),
    Location("Goron Mines Dangoro Chest", 0x804065D0, 0x40, True, 0x3),
    Location("Goron Mines Dungeon Reward", 0x804065D0, 0x8, True, 0x1D),
    Location("Goron Mines Entrance Chest", 0x804065D0, 0x8, True, 0x0),
    Location("Goron Mines Fyrus Heart Container", 0x804065D0, 0x10, True, 0x1D),
    Location("Goron Mines Gor Amato Chest", 0x804065D0, 0x2, True, 0x1),
    Location("Goron Mines Gor Amato Key Shard", 0x804069E0, 0x8, False, -1),
    Location("Goron Mines Gor Amato Small Chest", 0x804065D0, 0x1, True, 0x0),
    Location("Goron Mines Gor Ebizo Chest", 0x804065D0, 0x2, True, 0x0),
    Location("Goron Mines Gor Ezibo Key Shard", 0x804069E7, 0x2, False, -1),
    Location("Goron Mines Gor Liggs Chest", 0x804065D0, 0x4, True, 0x0),
    Location("Goron Mines Gor Liggs Key Shard", 0x804069E7, 0x1, False, -1),
    Location("Goron Mines Magnet Maze Chest", 0x804065D0, 0x10, True, 0x1),
    Location("Goron Mines Main Magnet Room Bottom Chest", 0x804065D0, 0x8, True, 0x2),
    Location("Goron Mines Main Magnet Room Top Chest", 0x804065D0, 0x40, True, 0x0),
    Location("Goron Mines Outside Beamos Chest", 0x804065D0, 0x80, True, 0x2),
    Location("Goron Mines Outside Clawshot Chest", 0x804065D0, 0x40, True, 0x2),
    Location("Goron Mines Outside Underwater Chest", 0x804065D0, 0x20, True, 0x1),
    Location("Goron Springwater Rush", -1, -1, -1, -1),
    Location("Herding Goats Reward", -1, -1, -1, -1),
    Location("Hidden Village Poe", -1, -1, -1, -1),
]
