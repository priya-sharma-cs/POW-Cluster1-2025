def word_search(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0

    # rows
    for r in range(rows):
        if word in ''.join(matrix[r]):
            return True
    # cols
    for c in range(cols):
        col_str = ''.join(matrix[r][c] for r in range(rows))
        if word in col_str:
            return True
    return False

if __name__ == "__main__":
    matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']
    ]
    print(word_search(matrix, "FOAM"))  # True
    print(word_search(matrix, "MASS"))  # True
    print(word_search(matrix, "FACE"))  # False
