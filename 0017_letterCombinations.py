"""
My ans
重點:
1.使用nested loop去控制迴圈要疊幾次
2.以str[:-1]去達到回溯的動作(抵銷該輪圈)
"""
class Solution(object):
    def __init__(self):
        self.ans = [] #解的list(最後結果)
        self.comb = '' #解

    def nested_loop(self, gl, digit_index, tt_digit):
        if digit_index == tt_digit: #選到最後一位數時，執行
            self.ans.append(self.comb)
            return
        for i in range(len(gl[digit_index])):
            self.comb += gl[digit_index][i] #把a放入comb,把d放入comb...g
            self.nested_loop(gl, digit_index+1, tt_digit) #呼叫自己變成nest,選到最後一位的時候將解(comb)加到ans就結束，如:adg
            self.comb = self.comb[:-1] #加入新解才會執行到這行，把這一位數的最後一個字母去掉(回溯概念)，然後在下一個迴圈中，加入該位的下一個數。
                                       #如 adg--(本行)-->ad--(下一輪迴圈開始)-->加入h，變成adh-->...-->adi-->ad
                                       #輪到i後，第三位數迴圈結束返回第二位數回圈的本行，ad--(本行)-->a--(下一輪迴圈開始)-->ae-->aeg...以此類推

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '': # digits is empty
            return []
    
        tt_digit = len(digits)
        dig_list = [ i for i in digits] # 234-> [2,3,4]
        map_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        gl = []
        for dig in dig_list:   # [2,3,4] -> ['abc','def',...]
            letters = map_dict[dig]
            gl.append(letters)

        self.nested_loop(gl, 0, tt_digit)

        return self.ans
"""
Better ans
1.把每一個解的每一位數依序發給每一個解作合併
  a->ad
   ->ae
   ->af
  b...
"""
class Solution(object):
    def letterCombinations(self, digits):
        if digits == "":
            return []

        numbers = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz",
        }

        res = [""]
                                #ex:[2,3,4] 
        for x in digits:        
            string = numbers[x] # string = abc, def
            new_res = []
            for y in res:     # res = '', a b c
                for z in string: 
                    new_res.append(y+z) # new_res = a b c, ad ae af bd...
            
            res = new_res
        
        return res

        
