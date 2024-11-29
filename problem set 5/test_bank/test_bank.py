from bank import bank
import pytest


def test_hello():
    assert bank("hello") == 0


def test_uppercase_hello():
    assert bank("HellO") == 0
    assert bank("HEN") == 20
    assert bank("NO") == 100


def test_not_hello():
    assert bank("How you doing?") == 20
    assert bank("cat") == 100
    assert bank("What's happening?") == 100


def test_num():
    with pytest.raises(TypeError):
        bank(1)
