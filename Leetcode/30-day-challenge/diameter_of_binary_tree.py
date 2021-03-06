# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3293/

"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diam = 1
        def depth(node):
            if not node: return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            self.diam = max(self.diam, left_depth + right_depth + 1)
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.diam - 1