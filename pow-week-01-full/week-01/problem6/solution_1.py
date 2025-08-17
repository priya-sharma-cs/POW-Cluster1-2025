from math import gcd
from functools import reduce

def gcd_n(nums):
    return reduce(gcd, nums)

if __name__ == "__main__":
    print(gcd_n([42,56,14]))  # 14
    print(gcd_n([8,16,32,64]))  # 8
