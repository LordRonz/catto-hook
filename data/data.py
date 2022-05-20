from base64 import b64decode
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

closings = [
    "THV2IHlh",
    "WE9YTw==",
    "TG92ZSB5b3U=",
    "TWlzc2luZyB5b3UgZXZlcnkgbW9tZW50",
    "VGhpbmtpbmcgb2YgeW91",
    "V2l0aCBsb3Zl",
    "TG90cyBvZiBsb3Zl",
    "U3RpbGwgdGhpbmtpbmcgb2YgeW91",
    "TXVjaCBsb3Zl",
    "QWxsIG15IGxvdmU=",
    "QWx3YXlz",
    "U2VuZGluZyB5b3UgYWxsIG15IGxvdmU=",
    "WW91ciBkZXZvdGVkIGxvdmVy",
    "VGUgYW1v",
    "V28gYWkgbmk=",
    "SmUgdCdhaW1l",
    "SWNoIGxpZWJlIGRpY2g=",
    "T25lIHdobyBoYXMgYmVlbiBtZXNtZXJpemVk",
    "QWxsIG15IGhlYXJ0",
    "VGFra2FuIHBlcm5haCBjYXBlayBiaWxhbmcgaWx5",
    "TXVuZ2tpbiBpbmkgYWxheSwgdGFwaSBiaWFyaW4=",
    "S2FsbyBrbSBtZXJhc2EgaW5pIGFsYXksIGJpbGFuZyB5YXA=",
    "QXlhZmx1",
    "SSA8MyB5b3U=",
    "YWt1IHNheWFuZyBrbQ==",
    "SSB3dXYgeW91",
    "QnVsYW5ueWEgaW5kYWggeWE=",
]


def get_closings():
    return f"{b64decode(choice(closings)).decode()}, A."

quotes = [
    "SSA8MyB5b3U=",
    "QWt1IHNheWFuZyBrYW11",
    "UGFnaSBtYW5pc2t1dQ==",
    "SWx5c20=",
    "SSB3dXYgeW91",
    "QnVsYW5ueWEgaW5kYWgga2VrIGtt",
    "QXlhZmx1",
]

def get_quotes():
    return b64decode(choice(quotes)).decode()
