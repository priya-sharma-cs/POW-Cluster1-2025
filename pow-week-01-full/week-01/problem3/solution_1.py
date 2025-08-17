def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]

if __name__ == "__main__":
    print(can_partition([15,5,20,10,35,15,10]))  # True
    print(can_partition([15,5,20,10,35]))        # False
