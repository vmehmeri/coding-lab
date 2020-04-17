# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3301/

"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_closing_needed = max_closing_needed = 0
        for char in s:
            if char == ")":
                max_closing_needed -= 1
            else:
                max_closing_needed += 1 
            
            if char == '(':
                min_closing_needed += 1 
            else:
                min_closing_needed = max(min_closing_needed - 1, 0)
            
            if max_closing_needed < 0: 
                return False
        
        return min_closing_needed == 0

solution = Solution()

examples = [
    "()", # True
    "(*)", # True
    "(*))", # True
    "((*))", # True
    "((*)", # True
    "()(*", # True
    "(()", # False
    "((*" # False
]

for ex in examples:
    print (
        solution.checkValidString(ex)
    )
    print("")