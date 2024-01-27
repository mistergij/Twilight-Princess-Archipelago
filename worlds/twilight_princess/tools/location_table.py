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
    Location("Arbiters Grounds East turning Room Poe", 0x80406610, 0x10, True, 0xA),
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
        "Arbiters Grounds West Stalfor Northeast Cave", 0x80406610, 0x1, True, 0x1
    ),
    Location("Arbiters Grounds West Stalfos West Chest", 0x80406610, 0x2, True, 0x1),
    Location("Ashei Sketch", -1, -1, -1, -1),
    Location("Auru Gift to Fyer", -1, -1, -1, -1),
    Location("Barnes Bomb Bag", 0x804069B9, 0x8, False, -1),
    Location("Bridge of Eldin Female Phasmid", -1, -1, -1, -1),
    Location("Bridge of Elldin Male Phasmid", -1, -1, -1, -1),
    Location("Bridge of Eldin Owl Statue Chest", -1, -1, -1, -1),
    Location("Bridge of Eldin Owl Statue Sky Character", -1, -1, -1, -1),
    Location("Bulbin Camp First Chest Under Tower At Entrance", -1, -1, -1, -1),
    Location("Bulbin Camp Poe", -1, -1, -1, -1),
    Location("Bulbin Camp Roasted Board", -1, -1, -1, -1),
    Location("Bulbin Camp Small Chest in Back of Camp", -1, -1, -1, -1),
    Location("Bulbin Guard Key", -1, -1, -1, -1),
    Location("Castle Town Malo Mart Magic Armor", -1, -1, -1, -1),
    Location("Cats Hide and Seek Minigame", -1, -1, -1, -1),
    Location("Cave of Ordeals Floor 17 Poe", -1, -1, -1, -1),
    Location("Cave of Ordeals Floor 33 Poe", -1, -1, -1, -1),
    Location("Cave of Ordeals Floor 44 Poe", -1, -1, -1, -1),
    Location("Cave of Ordeals Great Fairy Rewards", -1, -1, -1, -1),
    Location("Charlo Donation Blessing", -1, -1, -1, -1),
]
