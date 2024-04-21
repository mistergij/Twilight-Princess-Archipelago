# def link_tp_structures(world, player):
#     for exit, region in mandatory_connections:
#         world.get_entrance(exit, player).connect(world.get_region(region, player))

#     exits = [
#         exit.name
#         for r in world.regions
#         if r.player == player
#         for exit in r.exits
#         if exit.connected_region is None
#     ]
#     structs = [
#         r.name
#         for r in world.regions
#         if r.player == player and r.entrances == [] and r.name != "Menu"
#     ]
#     exits_spoiler = exits[:]

#     pairs = {}

#     def set_pair(exit, struct):
#         if (exit in exits) and (struct in structs):
#             pairs[exit] = struct
#             exits.remove(exit)
#             structs.remove(struct)
#         else:
#             raise Exception(
#                 f"Invalid connection: {exit} => {struct} for player {player} ({world.player_name[player]})"
#             )

#     if world.plando_connections[player]:
#         for conn in world.plando_connections[player]:
#             set_pair(conn.entrance, conn.exit)

#     for exit, struct in mandatory_connections:
#         if exit in exits:
#             set_pair(exit, struct)

#     try:
#         assert len(exits) == len(structs) == 0
#     except AssertionError:
#         raise Exception(
#             f"Failed to connect all Twilight Princess structures for player {player} ({world.player_name[player]})"
#         )

#     for exit in exits_spoiler:
#         world.get_entrance(exit, player).connect(world.get_region(pairs[exit], player))
#         if world.shuffle_structures[player] or world.plando_connections[player]:
#             world.spoiler.set_entrance(exit, pairs[exit], "entrance", player)


twilight_princess_regions = [
    ("Menu", ["New World"]),
    (
        "Ordona Province",
        [
            "Ordon Village - Links House Entrance",
            "Ordon Village - Mayor Bo House",
            "Ordon Village - Jaggle House",
            "Ordon Village - Rusl House",
            "Ordon Village - Sera Shop",
            "Ordon Ranch Entrance",
        ],
    ),
    ("South Faron Woods Entrance", []),
    ("Ordon Ranch", ["Ordon Ranch Grotto Entrance"]),
    ("Ordon Ranch Grotto", []),
    (
        "South Faron Woods",
        [
            "South Faron Woods Cave Entrance",
            "Faron Mist Area Entrance",
        ],
    ),
    ("Hyrule Field - Faron Field Entrance", []),
    ("South Faron Woods Cave", []),
    (
        "Faron Mist Area",
        ["Faron Mist Cave Entrance", "North Faron Woods Entrance"],
    ),
    ("Faron Mist Cave", []),
    ("North Faron Woods", ["Forest Temple Entrance", "Lost Woods Entrance"]),
    ("Lost Woods", ["Sacred Grove - Master Sword Area Entrance"]),
    (
        "Sacred Grove - Master Sword Area",
        [
            "Sacred Grove - Past Entrance"
            "Sacred Grove - Baba Serpent Grotto Entrance",
        ],
    ),
    ("Sacred Grove - Baba Serpent Grotto", []),
    ("Sacred Grove - Past", ["Temple of Time Entrance"]),
    (
        "Hyrule Field - Faron Field",
        ["Faron Field Corner Grotto Entrance"],
    ),
    ("Faron Field Corner Grotto", []),
    ("Kakariko Gorge Entrance", []),
    (
        "Kakariko Gorge",
        ["Eldin Lantern Cave Entrance"],
    ),
    ("Eldin Lantern Cave", []),
    ("Kakariko Village Entrance", []),
    (
        "Kakariko Village",
        ["Kakariko Graveyard Entrance", "Death Mountain Trail Entrance"],
    ),
    ("Kakariko Graveyard", []),
    ("Death Mountain Trail", ["Death Mountain Volcano Entrance"]),
    ("Death Mountain Volcano", ["Deth Mountain Interiors Entrance"]),
    ("Death Mountain Interiors", ["Goron Mines Entrance"]),
    ("Hyrule Field - Eldin Field Entrance", []),
    (
        "Hyrule Field - Eldin Field",
        [
            "Eldin Stockcave Entrance",
            "Eldin Field Water Bomb Fish Grotto Entrance",
            "Eldin Field Bomskit Grotto Entrance",
            "Eldin Field Stalfos Grotto Entrance",
        ],
    ),
    ("Eldin Stockcave", []),
    ("Eldin Field Water Bomb Fish Grotto", []),
    ("Eldin Field Bomskit Grotto", []),
    ("Eldin Field Stalfos Grotto", []),
    ("Hyrule Field - Lanayru Field Entrance", []),
    (
        "Hyrule Field - Lanayru Field",
        [
            "Hidden Village Entrance",
            "Lanayru Field Skulltula Grotto Entrance",
            "Lanayru Field Poe Grotto Entrance",
            "Lanayru Ice Puzzle Cave Entrance",
            "Zoras Domain Entrance",
        ],
    ),
    ("Hidden Village", []),
    ("Lanayru Field Skulltula Grotto", []),
    ("Lanayru Field Poe Grotto", []),
    ("Lanayru Ice Puzzle Cave", []),
    ("Outside Castle Town South Entrance", []),
    (
        "Outside Castle Town South",
        ["Outside South Castle Town Tektite Grotto Entrance"],
    ),
    ("Outside South Castle Town Tektite Grotto", []),
    ("Outside Castle Town West Entrance", []),
    ("Outside Castle Town West", ["West Hyrule Field Helmasaur Grotto Entrance"]),
    ("West Hyrule Field Helmasaur Grotto", []),
    ("Castle Town Entrance", []),
    ("Castle Town", ["Hyrule Castle Entrance"]),
    ("Lake Hylia Bridge Entrance", []),
    ("Lake Hylia Bridge", ["Lake Hylia Bridge Bubble Grotto Entrance"]),
    ("Lake Hylia Bridge Bubble Grotto", []),
    ("Lake Hylia Entrance", []),
    (
        "Lake Hylia",
        [
            "Lake Hylia Lantern Cave Entrance",
            "Lake Hylia Shell Blade Grotto Entrance",
            "Lake Hylia Water Toadpoli Grotto Entrance",
            "Lakebed Temple Entrance",
            "City in the Sky Entrance",
            "Gerudo Desert Entrance",
        ],
    ),
    ("Lake Hylia Lantern Cave", []),
    ("Lake Hylia Shell Blade Grotto", []),
    ("Lake Hylia Water Toadpoli Grotto", []),
    ("Zoras Domain", ["Snowpeak Climb Entrance"]),
    (
        "Snowpeak Climb",
        ["Snowpeak Summit Entrance", "Snowpeak Freezard Grotto Entrance"],
    ),
    ("Snowpeak Summit", ["Snowpeak Ruins Entrance"]),
    ("Snowpeak Freezard Grotto", []),
    (
        "Gerudo Desert",
        [
            "Bulblin Camp Entrance",
            "Cave of Ordeals Entrance",
            "Gerudo Desert Rock Grotto Entrance",
            "Gerudo Desert Skulltula Grotto Entrance",
        ],
    ),
    ("Bulblin Camp", ["Outside Arbiters Grounds Entrance"]),
    ("Gerudo Desert Rock Grotto", []),
    ("Gerudo Desert Skulltula Grotto", []),
    ("Cave of Ordeals Floors 01-11", ["Cave of Ordeals Floors 12-21 Entrance"]),
    ("Cave of Ordeals Floors 12-21", ["Cave of Ordeals Floors 22-31 Entrance"]),
    ("Cave of Ordeals Floors 22-31", ["Cave of Ordeals Floors 32-41 Entrance"]),
    ("Cave of Ordeals Floors 32-41", ["Cave of Ordeals Floors 42-50 Entrance"]),
    ("Cave of Ordeals Floors 42-50", []),
    ("Outside Arbiters Grounds", ["Arbiters Grounds Entrance"]),
    ("Forest Temple", []),
    ("Goron Mines", []),
    ("Lakebed Temple", []),
    ("Arbiters Grounds", []),
    ("Snowpeak Ruins", []),
    ("Temple of Time", []),
    ("City in the Sky", []),
    ("Hyrule Castle", []),
    ("Palace of Twilight", []),
]

mandatory_connections = []
