# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            current_root_val = preorder.pop(0)
            # Index of current root
            root_idx = inorder.index(current_root_val)
            
            root = TreeNode(current_root_val)
            root.left = self.buildTree(preorder, inorder[0:root_idx])
            root.right = self.buildTree(preorder, inorder[root_idx+1:])
            return root

        return None