from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    filled_jar = Jar(15)
    assert filled_jar.capacity == 15
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(15)
    jar.deposit(10)
    assert jar.size == 10


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3