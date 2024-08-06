import pytest

from bank import value


def test_lower():
    assert value("hello partrick") == 0
    assert value("herrow") == 20
    assert value("sakamlikum") == 100

def test_upper():
    assert value("HELLO BRO") == 0
    assert value("HERROW MALFOY") == 20
    assert value("S'UP") == 100


def test_up_low():
    assert value("Hello!") == 0
    assert value("hErrOW jUdE") == 20
    assert value("Ello Bro") == 100
