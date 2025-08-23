import solution1, solution2

def test():
    assert solution1.misere_nim(3,4,5) == True
    assert solution1.misere_nim(1,1,1) == False
    assert solution1.misere_nim(1,1,2) == True

    assert solution2.misere_nim_general([3,4,5]) == True
    assert solution2.misere_nim_general([1,1,1]) == False
    assert solution2.misere_nim_general([1,1,2]) == True

    print("All tests passed.")

if __name__ == "__main__":
    test()
