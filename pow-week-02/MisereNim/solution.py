def misere_nim(a, b, c):
    heaps = [a, b, c]
    if all(x == 1 for x in heaps):
        return len(heaps) % 2 == 0
    xor_val = a ^ b ^ c
    return xor_val != 0
