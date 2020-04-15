from typing import List

# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows_to_zero = set()
        cols_to_zero = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                current = matrix[row][col]
                if current == 0:
                    rows_to_zero.add(row)
                    cols_to_zero.add(col)
                elif row in rows_to_zero or col in cols_to_zero:
                    matrix[row][col] = 0
                    continue

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                current = matrix[row][col]
                if row in rows_to_zero or col in cols_to_zero:
                    matrix[row][col] = 0
                    continue

        

matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

Solution().setZeroes(matrix)
print(matrix)


