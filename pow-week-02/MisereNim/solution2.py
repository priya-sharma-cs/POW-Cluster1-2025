def misere_nim_general(heaps):
    if all(x == 1 for x in heaps):
        return len(heaps) % 2 == 0
    xor_val = 0
    for h in heaps:
        xor_val ^= h
    return xor_val != 0
