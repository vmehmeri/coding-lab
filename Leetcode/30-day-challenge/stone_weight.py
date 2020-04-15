# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3297/

"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

from typing import List
import heapq

class Solution:
    def _lastStoneWeight(self, stones: List[int]) -> int:
        def smash(stones, i, j):
            if stones[i] == stones[j]:
                stones.pop()
                stones.pop()
            else:
                stones[j] -= stones[i]
                stones.pop(i)
            
            stones.sort()
            

        stones.sort()
        while len(stones) > 1:
            index_of_largest = len(stones)-1
            index_of_second_largest = len(stones)-2
            smash(stones, index_of_second_largest, index_of_largest)

        if len(stones) == 1:
            return stones[0]

        return 0


    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [n*-1 for n in stones]
          
        def smash(stones):
            max_elem = heapq.heappop(stones)
            new_elem = max_elem - heapq.heappop(stones)
            if new_elem != 0:
                heapq.heappush(stones, new_elem)
            
            
        heapq.heapify(stones)    
        while len(stones) > 1:
            smash(stones)

        if len(stones) == 1:
            return -1*stones[0]

        return 0


print(
    Solution().lastStoneWeight(
        [2,7,4,1,8,1]
    )
)