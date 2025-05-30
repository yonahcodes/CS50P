import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25


def test_convert_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/3")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
