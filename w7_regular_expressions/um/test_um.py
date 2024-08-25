import pytest

from um import count


def test_just_um():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("um um um") == 3

def test_sentences():
    assert count("um!") == 1
    assert count("Thanks for, um, the ride.") == 1
    assert count("Um, hello") == 1
    assert count("Um, what's this, um... thingy?") == 2

def test_part_of_word():
    assert count("circumstances") == 0
    assert count("yummy") == 0
    assert count("instrument") == 0
    assert count("volume") == 0
