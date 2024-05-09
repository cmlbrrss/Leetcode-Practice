"""
My Ans
"""
class Solution(object):
    def selSort(self, nums, l, listLen):
        while l < listLen:
            minIdx = nums.index(min(nums[l:]),l)
            nums[minIdx], nums[l] = nums[l], nums[minIdx]
            l += 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        listLen = len(nums)
        for i in range(listLen - 2, -1, -1):
            for j in range(listLen - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    self.selSort(nums, i + 1, listLen)
                    return
        return self.selSort(nums, 0, listLen)
