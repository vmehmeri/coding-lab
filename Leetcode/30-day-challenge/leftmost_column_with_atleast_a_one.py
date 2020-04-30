"""
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

Example 1:
Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:
Input: mat = [[0,0],[0,1]]
Output: 1

Example 3:
Input: mat = [[0,0],[0,0]]
Output: -1

Example 4:
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 

Constraints:

1 <= mat.length, mat[i].length <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.

"""

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def __init__(self, matrix):
        self.dim = [len(matrix), len(matrix[0])] if matrix else [0,0]
        self.matrix = matrix
        self.get_count = 0

    def get(self, x: int, y: int) -> int:
        self.get_count += 1
        if self.get_count > 1000:
            raise "Ran get() too many times (1000)"
        return self.matrix[x][y]
    
    def dimensions(self):
        return self.dim

class Solution:
    # Binary Search solution
    def leftMostColumnWithOneBS(self, binaryMatrix: 'BinaryMatrix') -> int:
        num_rows, num_cols = binaryMatrix.dimensions()[0], binaryMatrix.dimensions()[1]
        if num_rows == 0:
            return -1

        def binarySearchForFirstOne(binaryMatrix, rowIndex, start, end):
            if end < start:
                return -1
            mid = (start + end) // 2
            if binaryMatrix.get(rowIndex,mid) == 1:
                if mid == 0:
                    return 0
                if binaryMatrix.get(rowIndex,mid-1)  == 0:
                    return mid
                return binarySearchForFirstOne(binaryMatrix, rowIndex, start, mid-1)
            else:
                return binarySearchForFirstOne(binaryMatrix, rowIndex, mid+1, end)

        leftmostColumnIndex = num_cols
        for i in range(num_rows):
            _leftmostColumnIndex = binarySearchForFirstOne(binaryMatrix, i, 0, num_cols-1)
            if _leftmostColumnIndex != -1:
                leftmostColumnIndex = min(leftmostColumnIndex,_leftmostColumnIndex)
        
        return leftmostColumnIndex if leftmostColumnIndex != num_cols else -1

    # Optimal Solution
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        M, N = binaryMatrix.dimensions()
        
        r, c = 0, N - 1 
        leftmost_col = -1
        while r < M and c >= 0:
            if binaryMatrix.get(r,c) == 1:
                leftmost_col = c
                c -= 1
            else:
                r += 1
        return leftmost_col

bm1 = BinaryMatrix([[0,0],[1,1]])
bm2 = BinaryMatrix([[0,0],[0,1]])
bm3 = BinaryMatrix([[0,0],[0,0]])
bm4 = BinaryMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])

s = Solution()

print(
    s.leftMostColumnWithOne(bm1), " Expected: 0"
)

print(
    s.leftMostColumnWithOne(bm2), " Expected: 1"
)

print(
    s.leftMostColumnWithOne(bm3), " Expected: -1"
)

print(
    s.leftMostColumnWithOne(bm4), " Expected: 1"
)