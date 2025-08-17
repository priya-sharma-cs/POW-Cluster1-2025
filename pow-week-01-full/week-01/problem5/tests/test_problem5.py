from solution_1 import flood_fill

def test_example():
    img = [
        ['B','B','W'],
        ['W','W','W'],
        ['W','W','W'],
        ['B','B','B']
    ]
    out = flood_fill(img, 2, 2, 'G')
    assert out == [
        ['B','B','G'],
        ['G','G','G'],
        ['G','G','G'],
        ['B','B','B']
    ]
