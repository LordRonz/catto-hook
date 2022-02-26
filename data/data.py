from secrets import choice

catmojis = [
    {
        "name": "SCblushy",
        "id": "834155037852696656",
        "animated": False,
    },
    {
        "name": "patpat",
        "id": "850326207874072658",
        "animated": True,
    },
    {
        "name": "petpetcat",
        "id": "829607417863995421",
        "animated": True,
    },
    {
        "name": "SCpetpetcat",
        "id": "676070904178016297",
        "animated": True,
    },
    {
        "name": "Cat",
        "id": "760379977320890398",
        "animated": True,
    },
    {
        "name": "SCsmack",
        "id": "780373520744054804",
        "animated": True,
    },
    {
        "name": "SCfall",
        "id": "664508741491752970",
        "animated": True,
    },
    {
        "name": "SChuggies",
        "id": "868468974571122718",
        "animated": True,
    },
    {
        "name": "SCWshakeblush",
        "id": "676858244391501824",
        "animated": True,
    },
    {
        "name": "SCdance",
        "id": "664513443675635732",
        "animated": True,
    },
    {
        "name": "SCGblush",
        "id": "664513356119539772",
        "animated": False,
    },
    {
        "name": "SCWblushHEART",
        "id": "753106557906190448",
        "animated": False,
    },
    {
        "name": "SCchilling",
        "id": "853896881532567572",
        "animated": True,
    },
    {
        "name": "SCcatkiss",
        "id": "750470459866480650",
        "animated": True,
    },
]


def get_catmoji():
    catmoji = choice(catmojis)
    return f"<{'a' if catmoji['animated'] else ''}:{catmoji['name']}:{catmoji['id']}>"


# https://discord.com/channels/305627343895003136/845532524724879380/907373349024432150
# https://discord.com/channels/747830885339889796/749030749591568484/792317725887168522
