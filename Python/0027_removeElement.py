"""
My Ans
題目:給予一個數列與一個指定目標數，使用原地演算法
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slowidx = 0
        for fastidx in range(len(nums)):
            if nums[fastidx] != val:
                nums[slowidx] = nums[fastidx]
                slowidx += 1

        return slowidx
