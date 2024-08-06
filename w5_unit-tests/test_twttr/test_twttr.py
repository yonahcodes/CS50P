import pytest

from twttr import shorten


def test_alpha_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("lazer") == "lzr"


def test_alpha_upper():
    assert shorten("GOOGLECHROME") == "GGLCHRM"
    assert shorten("TEST") == "TST"


def test_alphanum():
    assert shorten("cs50") == "cs50"
    assert shorten("Hai18") == "H18"


def test_punctuation():
    assert shorten("Bar.Yohai") == "Br.Yh"
    assert shorten("Hallo!") == "Hll!"
