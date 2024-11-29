import pytest
from plates import is_valid


def test_start_with_two_letters():
    assert is_valid("2C50") == False
    assert is_valid("CS50") == True
    assert is_valid("C205") == False


def test_length():
    assert is_valid("CSCS50") == True
    assert is_valid("C") == False
    assert is_valid("CS") == True
    assert is_valid("CSCS500") == False


def test_num_not_between_letters():
    assert is_valid("CS50cs") == False


def test_non_zero_first_num():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_has_punctuation():
    assert is_valid("CS50!") == False
    assert is_valid("CSCS5.") == False
