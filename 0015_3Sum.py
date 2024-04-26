""" 
My ans
1. 先將輸出以set方式宣告，並將nums由小到大排列
2. 從最小數(a)開始，a以右的數列最小及最大的數字分別為b跟c
3. 測試a + b + c大小，大於0則代表c太大，所以最大數要變小，所以次大數更新成最大數(r-1)，反之同理
"""
class Solution(object):            
    def threeSum(self, nums):
        anss = set()
        nums.sort()
        for i in range(len(nums)-2):
            a = nums[i]
            l = i + 1 # value>i的下一個數的index
            r = len(nums)-1 #最後的index = 長度-1
            while l < r :
                b = nums[l]
                c = nums[r]                
                if a + b + c == 0:
                    anss.add((a,b,c))
                    l += 1
                    r -= 1
                elif a + b + c > 0:
                    r -= 1
                else:
                    l += 1
                     
        return list(anss)

"""
Better Answer
1. 先將輸出以set方式宣告，並將nums分為+、-、0三組list
2. 先考慮三個0的特例
3. 再考慮(0, -p, p)的特例
4. 排除有0的數對(步驟2, 3)後，剩下的數對必定為(-,-,+)或(+,+,-)
5. 以(-,-,+)為例，先取負數的list(步驟1)，固定第一個數(a)，再用加上list以右一數(b)，
6. 因為a+b必定為負數，所以從正數的set中尋找是否有c = -(a+b)
7. 因為正數的list中有可能重複，但因為正數在(-,-,+)為唯一，所以是用set(正數的list)去做，減少迴圈次數
8. (+,+,-)同理
"""
class Solution(object):
    def threeSum(self, nums):
        res = set()
        pos,neg,z=[],[],0        
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                z += 1
        N,P=set(neg),set(pos)

        if z >= 3:
            res.add((0,0,0))
        
        if z >= 1:
            for p in pos:
                if -p in N:
                    res.add(tuple(sorted([0,-p,p])))
        
        for i,a in enumerate(pos):
            for b in pos[i+1:]:
                c=-(a+b)

                if c in N:
                    res.add(tuple(sorted([a,b,c])))
        
        for i,a in enumerate(neg):
            for b in neg[i+1:]:
                c=-(a+b)

                if c in P:
                    res.add(tuple(sorted([a,b,c])))

        return res
