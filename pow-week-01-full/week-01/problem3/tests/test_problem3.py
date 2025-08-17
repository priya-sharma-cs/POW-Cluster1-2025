from solution_1 import can_partition

def test_examples():
    assert can_partition([15,5,20,10,35,15,10]) is True
    assert can_partition([15,5,20,10,35]) is False
