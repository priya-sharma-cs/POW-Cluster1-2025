from solution_1 import word_search

def test_examples():
    matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']
    ]
    assert word_search(matrix, "FOAM") is True
    assert word_search(matrix, "MASS") is True
    assert word_search(matrix, "FACE") is False
