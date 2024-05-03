"""
My ans
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {'(':')', '[':']', '{':'}'}
        if len(s) % 2 != 0:
            return False
        while len(s) > 0:
            if '()' in s:
                idx = s.find('()')
                s = s[:idx] + s[idx+2:]
            elif '[]' in s:
                idx = s.find('[]')
                s = s[:idx] + s[idx+2:]
            elif '{}' in s:
                idx = s.find('{}')
                s = s[:idx] + s[idx+2:]
            else:
                return False
        return True

