from solution_1 import gcd_n

def test_examples():
    assert gcd_n([42,56,14]) == 14
    assert gcd_n([8,16,32,64]) == 8
    assert gcd_n([5]) == 5
    assert gcd_n([0, 10, 20]) == 10
