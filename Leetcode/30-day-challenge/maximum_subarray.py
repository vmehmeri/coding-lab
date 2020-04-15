# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return nums
        
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum += num
            # Reset current sum in case current number is 
            # greater (will be the case if there were negative numbers
            # in between that brought the sum down. So better to start
            # from current num in this case)
            current_sum = max(num, current_sum)
            # Update "global" max
            max_sum = max(max_sum, current_sum)

        return max_sum



s = Solution()

example = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(example))
