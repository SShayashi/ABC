class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        pair = [0, 0]
        for i in range(1, length):
            if nums[i-1] <= nums[i]:
                pair[0] = i-1
                pair[1] = i
        if pair == [0, 0]:
            nums.sort()
            return
        tmp = nums[pair[0]]
        first_min_i = nums.index(min(nums[pair[0]+1:]))
        nums[pair[0]] = nums[first_min_i]
        nums[first_min_i] = tmp
        subnums = nums[pair[0] + 1:]
        subnums.sort()
        sublen = len(subnums)
        for i in range(sublen):
            nums[i+pair[0]+1] = subnums[i]
        return


x = [2, 3, 1]
Solution().nextPermutation(x)
print(x)