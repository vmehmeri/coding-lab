# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/

"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

 

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 

Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
"""
from typing import List

class Solution:
    # Non-optimal solution
    def _stringShift(self, s: str, shift: List[List[int]]) -> str:
        final_str = s
        for sh in shift:
            direction = sh[0]
            amount = sh[1]
            if direction == 1: # shift right
                final_str = final_str[-amount:] + final_str[:-amount]
            else: # shift left
                final_str = final_str[amount:] + final_str[:amount]
        

        return final_str

    # Collapses operations together into one
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final_str = s
        # Assume a shift left
        final_direction = final_amount = 0
        for sh in shift:
            direction = sh[0]
            amount = sh[1]

            if direction == 0:
                final_amount += amount
            else: # a shift right can be thought of as a negative shift left
                final_amount -= amount
        
        if final_amount < 0: # it's a shift right in the end
            final_direction = 1
            final_amount = abs(final_amount)

        # A shift operation of the amount equal to the string's length
        # will just return the same string. And it will also cause the
        # code below to fail. Therefore, we take the modulo as the amount
        final_amount = final_amount % len(s)

        if final_direction == 1: # shift right
            final_str = final_str[-final_amount:] + final_str[:-final_amount]
        else: # shift left
            final_str = final_str[final_amount:] + final_str[:final_amount]
        

        return final_str


s = Solution()

s1 = "abc" 
shift1 = [[0,1],[1,2]]
s2 = "abcdefg" 
shift2 = [[1,1],[1,1],[0,2],[1,3]]

print(
    s.stringShift(s1, shift1)
)

print(
    s.stringShift(s2, shift2)
)
