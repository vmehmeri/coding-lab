# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

from collections import Counter
from typing import List

class Solution:
    """
        A solution that is linear in time but uses extra space.
    """
    def _singleNumber(self, nums: List[int]) -> int:
        # Creates counter dictionary. O(n) time and space.
        c = Counter(nums)

        # Iterate to find the one element with single count
        # O(n) time
        for num,count in c.items():
            if count == 1:
                return num

        return None
    
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        # XOR 0 with each num. Every number that has a pair will have
        # the XOR evaluated to 0. The single number with have the XOR
        # evaluated to itself. So in the end we will have the number.
        for n in nums:
            a ^= n
        
        return a

        


s = Solution()
example1 = [2,2,1]
print(s.singleNumber(example1))

example2 = [4,1,2,1,2]
print(s.singleNumber(example2))