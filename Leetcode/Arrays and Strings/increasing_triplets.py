# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781

"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""

from typing import List

class Solution:
    # [1, 3, 2, 0, 2, 7]
    # [1, 0, 3, 2, 2, -1, 4]
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        first_small, second_small, candidate_first, candidate_second = nums[0], None, None, None
        
        for num in nums:
            if second_small is not None and num > second_small:
                return True
            
            if candidate_second is not None and num > candidate_second:
                return True
            
            if second_small is None and first_small > num:
                first_small = num
                continue
                
            if second_small is None and first_small < num:
                second_small = num
                continue
                
            
            if second_small is not None and num > first_small and num < second_small:
                second_small = num
                continue
            
            if num < first_small and candidate_first is None or (candidate_first is not None and candidate_first > num):
                candidate_first = num
                
            elif candidate_first is not None and num > candidate_first and candidate_second is None or candidate_second is not None and candidate_second > num:
                candidate_second = num
                
        return False
                
        