# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3314/

"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    global_max = float('-inf')

    def maxPathSumRec(self, root):
        if not root:
            return 0
        
        
        max_left = self.maxPathSumRec(root.left)
        max_right = self.maxPathSumRec(root.right)
        if max_left < 0:
            max_left = 0
        if max_right < 0:
            max_right = 0
        self.global_max =  max(
            self.global_max,
            root.val + max_left + max_right)

        return max(max_left, max_right) + root.val

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPathSumRec(root)
        return self.global_max




        