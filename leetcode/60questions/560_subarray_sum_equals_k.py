from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        v = [nums[i] for i in range(len(nums))]
        for i in range(1, len(nums)):
            v[i] += v[i - 1]
        length = len(nums)
        ans = 0
        for x in range(length):
            for y in range(x, length):
                if x == y:
                    ans += 1 if v[x] == k else 0
                    continue
                ans += 1 if (v[y] - v[x]) == k else 0
        return ans


x = Solution()
a = x.subarraySum([1, 1, 1], 2)
print(a)
