"""
題目: 給定一遞增數列與目標，在數列中找到目標Index，若目標不存在數列，則找到插入位置的Index，以時間複雜度O(logn)撰寫
"""

"""
My Ans
重點:
  使用二分搜尋法
  情況考慮:
    1. target是否在nums中。若否，則須考慮插入位置
    2. 若不存在nums中則插入位置分為於中位數左與右，若此位置位於邊界會 Index OOR，必須另外處理
"""

class Solution(object):
    def __init__(self):
        self.origin = 0
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:      #確定有target不用考慮邊界情況
            midIdx = int(len(nums)/2)    ## 可化簡為 len(nums) // 2
            midNum = nums[midIdx]
            if midNum == target:
                return midIdx + self.origin
            elif midNum > target:                
                return self.searchInsert(nums[:midIdx], target)
            else:
                self.origin += midIdx
                return self.searchInsert(nums[midIdx:], target)
        else:
            
            ### 邊界情況 ###
            if target > nums[-1]:  #大於右邊界
                self.origin += len(nums)
                return self.origin
            elif target < nums[0]: #小於左邊界
                return self.origin

            ### 中間情況 ###
            midIdx = int(len(nums)/2)
            midNum = nums[midIdx]
            if midNum > target:
                if nums[midIdx - 1]  <  target:
                    self.origin += midIdx
                    return self.origin
                else:                
                    return self.searchInsert(nums[:midIdx], target)
            else:
                if nums[midIdx + 1]  >  target:
                    self.origin += (midIdx + 1)
                    return self.origin
                else:
                    self.origin += midIdx
                    return self.searchInsert(nums[midIdx:], target)

"""
Better Ans
"""

class Solution(object):
    def searchInsert(self, nums, target):
        lower = 0
        upper = len(nums) - 1

        ### 邊界情況 ###
        if target <= nums[0]:
            return 0

        elif target > nums[-1]:
            return len(nums)
          
        ### 非邊界情況 ###
        while (lower + 1) < upper:      # 將下邊界更新mid
            mid = (upper + lower) // 2

            if target > nums[mid]:  # 將下邊界更新mid
                lower = mid

            elif target < nums[mid]:
                upper = mid

            else:     # nums[mid]為target
                return mid

        return lower + 1
