from data.data import closings
from base64 import b64decode, b64encode


def test_closing():
    for closing in closings:
        decoded = b64decode(closing)
        encoded = b64encode(decoded).decode()
        assert encoded == closing
