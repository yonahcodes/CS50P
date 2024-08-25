import pytest

from working import convert


def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("1 PM to 7 AM") == "13:00 to 07:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("12:00 AM to 5:00 AM") == "00:00 to 05:00"


def test_hours_minutes():
    assert convert("9:21 AM to 5:11 PM") == "09:21 to 17:11"
    assert convert("4:59 AM to 7:15 PM") == "04:59 to 19:15"
    assert convert("1:13 AM to 11:00 PM") == "01:13 to 23:00"


def test_exception():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 24:00 PM")
