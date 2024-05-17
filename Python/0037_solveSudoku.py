class Solution(object):
    def judge(self, rowIdx, colIdx, num, board):
        for i in range(9):                  #檢查同列  
            if num == board[rowIdx][i]:
                return False

        for j in range(9):                  #檢查同行
            if num == board[j][colIdx]:
                return False

        boxL = (rowIdx // 3) * 3            #檢查同格
        boxU = (colIdx // 3) * 3
        for i in range(boxL, boxL + 3):
            for j in range(boxU, boxU + 3):
                if num == board[i][j]:
                    return False
        return True

    def backtracking(self, board):
        for rowIdx in range(9):
            for colIdx in range(9):
                if board[rowIdx][colIdx] != '.':
                    continue
                for num in range(1,10):
                    if self.judge(rowIdx, colIdx, str(num), board):
                        board[rowIdx][colIdx] = str(num)
                        if self.backtracking(board):
                            return True
                        board[rowIdx][colIdx] = '.'
                return False
        return True

    def solveSudoku(self, board):
        """
        cell: 目標小格子中的數字
        num: 泛指1~9，填入的數字
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        self.backtracking(board)
