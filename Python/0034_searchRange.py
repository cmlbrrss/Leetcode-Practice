"""
My Ans
"""
class Solution(object):
    def __init__(self):
        self.origin = 0
    def searchRange(self, nums, target):
        if nums == [] or target not in nums:  #空數列或target不存在
            return [-1, -1]

        if len(nums) == 1 and target in nums:
            print(self.origin)
            return [self.origin, self.origin]

        if len(nums) == 2 and target in nums:
            if nums[0] == target:
                if nums[1] == target:
                    return [self.origin, self.origin + 1]
                else:
                    return [self.origin, self.origin]
            else:
                return [self.origin + 1, self.origin + 1]

        midIdx = int(len(nums) / 2)
        midNum = nums[midIdx]
        if midNum == target:
            maxIdx = midIdx
            minIdx = midIdx
            if nums[-1] == target:
                maxIdx = len(nums) - 1
            else: 
                while nums[maxIdx + 1] == target:
                    maxIdx += 1
            if nums[0] == target:
                minIdx = 0
            else: 
                while nums[minIdx - 1] == target:
                    minIdx -= 1
            return [self.origin + minIdx, self.origin + maxIdx]
        elif midNum < target:
            self.origin += midIdx
            return self.searchRange(nums[midIdx:], target)
        elif midNum > target:
            return self.searchRange(nums[:midIdx], target)
            
