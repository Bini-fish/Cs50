from um import count

def test_um():
    assert count("Um, thanks for the album") == 1
    assert count("um") == 1
    assert count("Um, thanks, um...") == 2
    assert count("um?") == 1
    assert count("Yummy") == 0
    assert count("Um? Mum?") == 1
    assert count("Um, thanks, um, regular expressions make sense now.") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

