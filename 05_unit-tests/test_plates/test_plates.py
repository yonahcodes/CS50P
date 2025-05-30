import pytest

from plates import is_valid


def test_starts_2_letters():
    assert is_valid("HELLO") == True
    assert is_valid("AE332") == True
    assert is_valid("A3356") == False
    assert is_valid("5566O") == False


def test_min_2_characters():
    assert is_valid("H") == False
    assert is_valid("AA") == True
    assert is_valid("5") == False
    assert is_valid("AA5") == True


def test_max_6_letters():
    assert is_valid("LAZERY") == True
    assert is_valid("GOODBYE") == False
    assert is_valid("EMET26") == True
    assert is_valid("OK84567") == False


def test_number_placement():
    assert is_valid("AA1826") == True
    assert is_valid("AAA222") == True
    assert is_valid("CS50P") == False
    assert is_valid("ZZ44TP") == False


def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_special_characters():
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("PI3.14") == False
    assert is_valid("YO700!") == False
