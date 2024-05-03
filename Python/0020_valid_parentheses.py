"""
My ans(Slow)
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

"""
My ans(Fast)
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
        i = 0
        close = ''
        for i in range(len(s)):
            if s[i] in mapping.keys():
                close += mapping[s[i]]
            else:
                if close == '' or s[i] != close[-1]:
                    return False
                else:
                    close = close[:-1]
        if close == '':
            return True
        else:
            return False

