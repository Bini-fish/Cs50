import pytest
from tabulate import tabulate
from project import valid_date, is_name, is_phone_num, is_url, menu, get_client, format_client, add_client, edit_client, remove_client


def test_valid_date():
    with pytest.raises(ValueError):
        assert valid_date('2025-55-13')


def test_name():
    with pytest.raises(SystemExit):
        assert is_name("benj2")


def test_phone_num():
    with pytest.raises(SystemExit):
        assert is_phone_num("+2519236598742")
        assert is_phone_num("09012341061")


def test_url():
    with pytest.raises(SystemExit):
        assert is_url("https://www.instagram.com")
        assert is_url("www.instagram.com")
        assert is_url("www.ethioware.org")


def test_menu():
    with pytest.raises(SystemExit):
        assert menu("2")
        assert menu(5)
