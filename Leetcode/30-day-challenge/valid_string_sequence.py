# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/

"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not arr:
            return True
        
        def isValidSequenceHelper(root, arr, start):
            if not root:
                return False
            if start == len(arr)-1:
                return root.val == arr[start] and root.left == None and root.right == None
            
            
            
            return root.val == arr[start] and (
                isValidSequenceHelper(root.left, arr, start+1) or 
                isValidSequenceHelper(root.right, arr, start +1)
                )

        return isValidSequenceHelper(root, arr, 0)
        