from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d[num] + 1 if d.get(num, 0) else 1

        tmp = list(d.items())
        tmp.sort(key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(tmp[i][0])
        return ans


def maxheaplify(nums: List[int], i):
    left = nums[i * 2 + 1]
    right = nums[i * 2 + 2] if (i * 2 + 2) < len(nums) else -9999999
    large_child_i = i * 2 + 1 if left > right else i * 2 + 2
    if nums[i] < nums[large_child_i]:
        nums[i], nums[large_child_i] = nums[large_child_i], nums[i]
        maxheaplify(nums, i // 2)


def heaplify(nums: List[int]):
    length = len(nums)
    for i in reversed(range(length // 2)):
        maxheaplify(nums, i)
    return nums


y = [3, 5, 6, 8, 2, 3, 4, 5, 21, 1, 4, 5, 7, 9, 2, 22]
print(heaplify(y))
