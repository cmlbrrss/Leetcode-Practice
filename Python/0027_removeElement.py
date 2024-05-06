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
