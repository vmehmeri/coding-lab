# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3302/
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

from typing import List
from collections import defaultdict
class Solution:
    _visited = defaultdict(lambda: False)
    def numIslands(self, grid: List[List[str]]) -> int:
        self._visited = defaultdict(lambda: False)
        if not grid:
            return 0
            
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if int(grid[row][col]) == 1 and not self._visited[(row,col)]:
                    # traverse all "connected ones" to mark them as "visited" (i.e. part of an island already counted)
                    self._dfs(grid, row, col) 
                    count += 1 # start of a new island
        return count

    def _out_of_bounds(self, grid, i, j):
        return i<0 or j<0 or i>=len(grid) or j>=len(grid[0])

    def _dfs(self, grid, i, j):
        if self._out_of_bounds(grid,i,j) or int(grid[i][j]) != 1 or self._visited[(i,j)]:
            return
        
        self._visited[(i,j)] = True

        self._dfs(grid, i+1, j)
        self._dfs(grid, i-1, j)
        self._dfs(grid, i, j+1)
        self._dfs(grid, i, j-1)


s = Solution()

example1 = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
]

print(s.numIslands(example1))

example2 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]

print(s.numIslands(example2))

example3 = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]

print(s.numIslands(example3))