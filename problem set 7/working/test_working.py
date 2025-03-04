from working import convert
import pytest

def test_case1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
def test_wrong_minute():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
def test_error():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("8:60 AM to 4:60 PM")
        convert("09:00 AM - 17:00 PM")
        convert("9 to 5")