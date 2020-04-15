# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3298/

"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

"""

from typing import List

class Solution:
    # Method 1: Brute Force
    def _findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        for start in range(len(nums)-1):
            zero_count = one_count = 0
            for end in range(start,len(nums)):
                if nums[end] == 1:
                    one_count += 1
                else:
                    zero_count += 1
                if one_count == zero_count:
                    ans = max(ans, end-start+1)
                    
        
        return ans

    # Method 2: Count Hashmap
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        count_up_to_here = 0
        seen_at = {}

        seen_at[count_up_to_here] = 0
        for i,num in enumerate(nums):
            current_pos = i + 1
            count_up_to_here = count_up_to_here + (1 if num else -1)
            if count_up_to_here not in seen_at:
                seen_at[count_up_to_here] = current_pos
            else:
                ans = max(ans, current_pos-seen_at[count_up_to_here])
                    
        return ans


examples = [
    [0,1],
    [0,1,0],
    [0,0,1,0,0,0,1,0,1,1,1,0]
]

s = Solution()

for e in examples:
    print(
        s.findMaxLength(e)
    )
        