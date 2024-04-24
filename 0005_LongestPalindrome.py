## My Ans 
class Solution(object):
    def pal_judge(self, pal):
        l = len(pal)
        for i in range(int(l/2)):
            if pal[i] != pal[l-i-1]:
                return False
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_pal = ''
        if len(s) == 1:
            max_pal = s
        for i in range(len(s)-1, 0, -1):
            pal_int = s[i]
            sts = [idx for idx,char in enumerate(s) if char == pal_int]
            for st in sts:
                if len(sts) == 1: #無回文
                    pal = pal_int
                else:
                    pal = s[st:i+1] 
                    judge = self.pal_judge(pal)
                    if judge:                        
                        break
            if len(pal) > len(max_pal):
                max_pal = pal
        return max_pal
