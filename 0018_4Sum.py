"""
My ans (For迴圈+雙指針)
"""
class Solution(object):
    def __init__(self):
        self.ans = []

    def twoPointer(self, nums, a, a_idx, target):
        for j in range(a_idx+1,len(nums)):
            b = nums[j]
            print(b,nums[j-1])
            if j >= a_idx+2 and b == nums[j-1]:
                continue
            if a + b > target and target > 0:
                break
            l = j + 1
            r = len(nums) - 1
            while l < r:
                c = nums[l]
                d = nums[r]
                if a + b + c + d == target:
                    self.ans.append([a, b, c, d])
                    while l < r and c == nums[l + 1]:
                        l += 1
                    while l < r and d == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif a + b + c + d > target:
                    r -= 1
                else:
                    l += 1

    def fourSum(self, nums, target):
        nums.sort()
        for i in range(len(nums)):
            a = nums[i]
            if i >= 1 and a == nums[i-1]: #刪去重複的，nums[i-1] == nums[i]的話能配出的結果必定一樣 
                continue
            if a > target and target > 0: #因為a為最小數，所以當target>0時，則無其他組合。若target<0，則不成立，
                break                     #例:a = -4,target = -10，可透過其他比-4大的負數，-3, -2, -1相加成-10
            self.twoPointer(nums, a, i, target)

        return self.ans

