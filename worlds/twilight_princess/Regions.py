def link_tp_structures(world, player):
    for exit, region in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))

    exits = [
        exit.name
        for r in world.regions
        if r.player == player
        for exit in r.exits
        if exit.connected_region is None
    ]
    structs = [
        r.name
        for r in world.regions
        if r.player == player and r.entrances == [] and r.name != "Menu"
    ]
    exits_spoiler = exits[:]

    pairs = {}

    def set_pair(exit, struct):
        if (exit in exits) and (struct in structs):
            pairs[exit] = struct
            exits.remove(exit)
            structs.remove(struct)
        else:
            raise Exception(
                f"Invalid connection: {exit} => {struct} for player {player} ({world.player_name[player]})"
            )

    if world.plando_connections[player]:
        for conn in world.plando_connections[player]:
            set_pair(conn.entrance, conn.exit)

    for exit, struct in mandatory_connections:
        if exit in exits:
            set_pair(exit, struct)

    try:
        assert len(exits) == len(structs) == 0
    except AssertionError:
        raise Exception(
            f"Failed to connect all Twilight Princess structures for player {player} ({world.player_name[player]})"
        )

    for exit in exits_spoiler:
        world.get_entrance(exit, player).connect(world.get_region(pairs[exit], player))
        if world.shuffle_structures[player] or world.plando_connections[player]:
            world.spoiler.set_entrance(exit, pairs[exit], "entrance", player)


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
            "South Faron Woods Entrance",
        ],
    ),
    ("Ordon Ranch", ["Ordon Ranch Grotto Entrance"]),
    ("Ordon Ranch Grotto", []),
    (
        "South Faron Woods",
        [
            "South Faron Woods Cave Entrance",
            "Faron Mist Area Entrance",
            "Hyrule Field - Faron Field Entrance",
        ],
    ),
    ("South Faron Woods Cave", []),
    ("Faron Mist Area", []),
    ("Hyrule Field - Faron Field", []),
]

mandatory_connections = []
