class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        length = len(nums)
        p = 0
        for i in range(length - 2, 0, -1):
            if nums[i+1] > nums[i]:
                p = i
                break
        if p == 0:
            rev(nums, 0, length - 1)
            return

        j = 0
        # 右に行くほど小さいはず，そのなかで右から数えて一，num[p]より番大きいものを探したい
        for i in range(length - 1, -1, -1):
            if nums[i] > nums[p]:
                j = i
                break
        nums[p], nums[j] = nums[j], nums[p]
        rev(nums, p+1, length-1)
        return


# x = [1,2,3]
x = [2,3,1,3,3]
Solution().nextPermutation(x)
print(x)