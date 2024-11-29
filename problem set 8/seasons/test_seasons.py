from seasons import valid_bday
import pytest

def test_correct():
    assert valid_bday("1999-01-01") == "Thirteen million, five hundred thirty-four thousand, five hundred sixty minutes"
    
def test_corrected():
    assert valid_bday("2023-09-25") == "Five hundred twenty-seven thousand forty minutes"

def test_error():
    with pytest.raises(SystemExit):
        valid_bday("January 1, 1999")