# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3307/

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

from typing import List
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter()
        counter[0] = 1
        ans = c_sum = 0
        for num in nums:
            c_sum += num
            ans += counter[c_sum-k]
            counter[c_sum] += 1
        return ans


s = Solution()

example1 = [1,1,1]
k = 2

print(
    s.subarraySum(example1, k)
)