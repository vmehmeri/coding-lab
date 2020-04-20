# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3303/

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Recursive solution. Time limit exceeded
        def _minPathSumRec(grid, start_i, start_j):
            if start_i >= len(grid) or start_j >= len(grid[0]):
                return float('inf')

            starting_elem = grid[start_i][start_j]
            if start_i == len(grid) - 1 and start_j == len(grid[0]) - 1:
                return starting_elem

            min_from_here = min(
                _minPathSumRec(grid,start_i+1, start_j),
                _minPathSumRec(grid,start_i, start_j+1)
            )

            return starting_elem + min_from_here if min_from_here < float('inf') else 0

        def minPathSumDP(grid):
            min_path_dict = { } # key: (i,j), value: min path

            i = len(grid)-1
            j = len(grid[0])-1

            min_path_dict[(i,j)] = grid[i][j]
            _i = i-1
            _j = j-1
            while _i>=0:
                min_path_dict[(_i,j)] = min_path_dict[(_i+1,j)] + grid[_i][j]
                _i -= 1
            while _j>=0:
                min_path_dict[(i,_j)] = min_path_dict[(i,_j+1)] + grid[i][_j]
                _j -= 1

            for _i in range(len(grid)-2,-1,-1):
                for _j in range(len(grid[0])-2,-1,-1):
                    min_path_dict[(_i,_j)] = grid[_i][_j] + min(min_path_dict[(_i+1,_j)], min_path_dict[(_i,_j+1)])

            return min_path_dict[(0,0)]

        if not grid:
            return 0

        return minPathSumDP(grid)

s = Solution()

example = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]



print(
    s.minPathSum(example)
)

