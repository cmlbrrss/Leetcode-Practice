## My Ans 
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

