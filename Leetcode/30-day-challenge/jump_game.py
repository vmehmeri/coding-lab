# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3310/

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable_from_here = set() # set of indexes
        if not nums:
            return False
        if len(nums) == 1:
            return True
        last = len(nums)-1

        for i in range(last-1,-1,-1):
            val = nums[i]
            if val >= last-i:
                reachable_from_here.add(i)
            else:
                for j in reachable_from_here:
                    if val >= j-i:
                        reachable_from_here.add(i)
                        break
        
        return 0 in reachable_from_here


s = Solution()
example1 = [2,3,1,1,4]

print(
    s.canJump(example1)
)

example2 = [3,2,1,0,4]

print(
    s.canJump(example2)
)