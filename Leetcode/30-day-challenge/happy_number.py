# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def splitToDigits(n):
            return [int(d) for d in str(n)]
        
        square_sum = 0
        current_num = n
        seen = set()
        
        while True:
            for digit in splitToDigits(current_num):
                square_sum += digit**2
            
            if square_sum in seen:
                return False

            if square_sum == 1:
                return True

            seen.add(square_sum)
            current_num = square_sum
            square_sum = 0

            


        return False

examples = [19, 82, 68, 45, 1, 10, 12, 31]

s = Solution()

for example in examples:
    print (example, s.isHappy(example))


