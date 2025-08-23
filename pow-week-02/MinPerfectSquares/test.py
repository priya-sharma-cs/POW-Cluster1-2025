import solution1, solution2

def test():
    for func in [solution1.numSquares, solution2.numSquares]:
        assert func(13) == 2
        assert func(27) == 3
        assert func(1) == 1
    print("All tests passed.")

if __name__ == "__main__":
    test()
