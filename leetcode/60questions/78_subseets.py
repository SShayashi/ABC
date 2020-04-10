from typing import List


import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)+1):
            for j in itertools.combinations(nums, i):
                ans.append(list(j))
        return ans



x = Solution()
print(x.subsets([1,2,3]))