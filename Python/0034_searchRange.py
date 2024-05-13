"""
題目:給定一個遞增數列(非嚴格遞增)與目標，返回目標的最小與最大Index
"""

"""
My Ans
重點:
使用遞迴函數時，要return接自我調用，否則會return None

錯誤寫法，如:
    def func(...):
        if cond:
            self.func(...) 
        else:
            return ...    
舉例可參考: https://blog.csdn.net/Ha_hha/article/details/79393041
理由:
最後一個遞迴(假設為第N個遞迴)有正常return，然後程式就會回去跑第N - 1個遞迴剩下的指令，但剩餘指令中未執行到其他return，所以第N - 1個遞迴return值為None，同理第N - 2, 第N - 3...第1個遞迴
第1個遞迴因為return值為None，所以最後輸出為None而非正常return。

整確的寫法，要return接自我調用，如:
    def func(...):
        if cond:
            return self.func(...)
        else:
            return ...
        
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
            
