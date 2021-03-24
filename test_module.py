import module

def test_binom1():
    a = 1
    b = 2
    expected = 9
    actual = module.binom1(a, b)
    assert expected == actual