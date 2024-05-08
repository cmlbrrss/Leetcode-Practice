class Solution(object):
    def strStr(self, haystack, needle):
        ans = haystack.find(needle)

        return ans

class Solution(object):
    def strStr(self, haystack, needle):
        nLen = len(needle)
        i = 0
        while i+nLen <= len(haystack):
            if haystack[i:i+nLen] == needle:
                return i
            i += 1
        return -1
