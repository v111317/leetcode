#https://leetcode.com/problems/game-of-life/description/

# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised 
# by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) 
# or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
# using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, 
# where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
from typing import List

class Solution:
    #try solving using O(1) space
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        neighbourMap = {}
        count = 0
        for i in range(rows):
            count = 0
            for j in range(cols):
                if i-1>=0:
                    if j-1>=0:
                        count += board[i-1][j-1]
                    if j+1<cols:
                        count += board[i-1][j+1]
                    count += board[i-1][j]
                    
                if j-1>=0:
                    if i+1<rows:
                        count += board[i+1][j-1]
                    count += board[i][j-1]
                    
                if i+1<rows:
                    if j+1<cols:
                        count += board[i+1][j+1]
                    count += board[i+1][j]
                
                if j+1<cols:
                    count += board[i][j+1]
                
                key = str(i) + "_" + str(j)
                neighbourMap[key] = count
                count = 0 
        print(neighbourMap)
        for i in range(rows):
            for j in range(cols):
                key = str(i) + "_" + str(j)
                if board[i][j]==0: 
                    if neighbourMap[key]==3:
                        board[i][j] = 1
                else:
                    neighbour = neighbourMap[key]
                    if neighbour<2:
                        board[i][j] = 0
                    elif neighbour in [2,3]:
                        board[i][j] = 1
                    elif neighbour > 3:
                        board[i][j] = 0
        
sol1 = Solution()
# mat1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# sol1.gameOfLife(mat1)
# print(mat1)
mat2 = [[1,1],[1,0]]
sol1.gameOfLife(mat2)
print(mat2)

                    