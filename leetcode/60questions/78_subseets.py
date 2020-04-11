from typing import List

"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)+1):
            for j in itertools.combinations(nums, i):
                ans.append(list(j))
        return ans

"""

# solution 2
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            new = []
            # どんどんfor分の要素が長くなっていきつつ，for-loop回す場合として覚えておきたい
            for curr in output:
                new.append(curr + [num])
            for n in new:
                output.append(n)

        return output
"""
""" Solution 3
backtrack完全に理解した，解空間の深さ優先をしている
また[:] は .copy() と等価
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            print("k:", k, "first:", first, "curr:", curr)
            if len(curr) == k:
                output.append(curr[:])

            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return output
"""


class Solution():
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(2 ** n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]
            ans.append([i for i in range(1, 4) if bitmask[i - 1] == '1'])

        return ans


x = Solution()
print(x.subsets([1, 2, 3]))
