# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/
from typing import List
from collections import deque 

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def inorderTraversalRec(root_node):
            if not root_node:
                return None

            left = inorderTraversalRec(root_node.left)
            
            if left:
                result.append(left)
            
            result.append(root_node.val)

            right = inorderTraversalRec(root_node.right)

            if right:
                result.append(right)

        def inorderTraversalIter(root_node):
            node_stack = []
            node_parents = {}
            node_ptr = root_node

            def addLeftTreeToStack(node):
                pass

            def addRightTreeToStack(node):
                pass

            while node_ptr.left is not None:
                node_parents[node_ptr.left] = node_ptr
                node_ptr = node_ptr.left
            
            node_stack.append(node_ptr.val)

            while node_ptr in node_parents:
                node_stack.append(node_parents[node_ptr])


        inorderTraversalRec(root)

        return result

input_tree = TreeNode(1)
input_tree.right = TreeNode(2)
input_tree.right.left = TreeNode(3)

s = Solution()

print(s.inorderTraversal(input_tree))