"""
題目:找到字串中最常回文 並返回回文
"""

"""
My First Ans
"""
class Solution(object):
    def pal_judge(self, pal):
        if pal == pal[ : :-1]:
            return True
        else:
            return False

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_pal = ''
        if len(s) == 1:  ## s長度 = 1
            max_pal = s
        for i in range(len(s)-1, 0, -1):
            pal_int = s[i]
            st = s.find(pal_int)
            if st == -1 : #無字尾,必無回文
                pal = pal_int
            else: #有字尾
                sts = [idx for idx, letter in enumerate(s) if letter == pal_int]
                for st in sts:
                    pal = s[st:i+1]
                    judge = self.pal_judge(pal)
                    if judge: #有回文
                        break
                if len(pal) > len(max_pal):
                    max_pal = pal
        return max_pal

"""
Better Solution (600ms)
"""
def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """
            max_pal = ''
            for n in range(len(s)): #有中心的回文(回文長度為odd)，如'aba'
                i = j = n
                while ((i >= 0 and j < len(s)) and s[i] == s[j]): #由第n個字母向字首和字尾延伸，前半確保不會string out of range，後半判斷回文
                    pal = s[i:j+1]
                    i -= 1
                    j += 1
                max_pal = max(max_pal, pal, key=len)

            for n in range(len(s)): #無中心的回文(回文長度為even)，如:'aa'
                i = n
                j = n + 1
                while ((i >= 0 and j < len(s)) and s[i] == s[j]): 
                    pal = s[i:j+1]
                    i -= 1
                    j += 1
                max_pal = max(max_pal, pal, key=len)

            return max_pal

"""
Best Solution
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[ : : -1] :
            return s
        
        start, size = 1,0
        for i in range (1,len(s)):
            start,r = i-size,i+1  #l為回文頭, r回文尾(第i個字)
            s1,s2 = s[start-1:r],s[start:r] # s2 = [第i-size 到 第i]。若size = 0，則 s2 = [第i 到 第i]    i,size,start,r  (1,0,1,2),(2,1,1,2) 
            if l-1 >=0 and s1 == s1[::-1]:  
                start,size = start-1,size+2
            elif s2 == s2[::-1]: # 回文頭更新為i，size更新為1
                start,size = start,size+1
                
        return s[start : start + size]
        
        
