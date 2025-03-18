from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        f = nums.copy()
        for i in range(k):
            minimum = min(f)
            index = f.index(minimum)
            f[index] = f[index] * multiplier
        return f


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    k = 3
    multiplier = 3
    s = Solution()
    print(s.getFinalState(nums, k, multiplier))