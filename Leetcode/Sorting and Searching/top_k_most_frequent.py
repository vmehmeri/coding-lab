# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/

"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""

from typing import List
from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fd = {} # frequency dictionary
        fd = Counter(nums)
        min_heap = []
        top_k_frequent = []
        
        for num,f in fd.items():
            if len(min_heap) < k:
                heappush(min_heap, (f,num))
            else:
                if f > min_heap[0][0]:
                    heappop(min_heap)
                    heappush(min_heap, (f,num))
        
        for f,n in min_heap:
            top_k_frequent.append(n)

        return top_k_frequent




print(
    Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)
)