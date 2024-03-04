#https://leetcode.com/problems/valid-sudoku/description/

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to 
# the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = 1
        colMap = [{} for i in range(0,9)]
        sqMap = [{} for i in range(0,3)]
        
        for i in range(0, 9):
            row = board[i]
            rowMap = {}
            for j in range(0, 9):
                cell = row[j]
                if cell == ".":
                    continue
                if cell in rowMap:
                    return False
                else:
                    rowMap[cell] = 1
                if cell in colMap[j]:
                    return False
                else:
                    colMap[j][cell] = 1
                
        print(colMap)
        return True

sol1 = Solution()
s1 = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]
print(sol1.isValidSudoku(s1))

        