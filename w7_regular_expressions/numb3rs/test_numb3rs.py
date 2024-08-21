import pytest


from numb3rs import validate


def test_one_digit():
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("9.9.9.-9") == False


def test_two_digits():
    assert validate("11.19.99.50") == True
    assert validate("10.20.30.40") == True
    assert validate("99.ct.-3.00") == False
    assert validate("99,00,10,42") == False


def test_three_digits():
    assert validate("255.255.255.255") == True
    assert validate("100.172.255.211") == True
    assert validate("512.512.512.512") == False
    assert validate("255.198.422.111") == False


def test_mixed_digits_or_alpha():
    assert validate("255.0.198.4") == True
    assert validate("0.154.254.9") == True
    assert validate("hello") == False
    assert validate("4.256.999.0") == False
    assert validate("1.198.Hi.0") == False
