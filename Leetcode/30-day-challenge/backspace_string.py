# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/

"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if not S and not T:
            return True
        
        s_stack = []
        t_stack = []

        for char in S:
            if not s_stack and char == "#":
                continue
            elif char != "#":
                s_stack.append(char)
            elif char == "#":
                s_stack.pop()

        for char in T:
            if not t_stack and char == "#":
                continue
            elif char != "#":
                t_stack.append(char)
            elif char == "#":
                t_stack.pop()

        return s_stack == t_stack

s = Solution()

examples = [
    ("ab#c", "ad#c"),
    ("ab##", "c#d#"),
    ("a##c", "#a#c"),
    ("a#c", "b")
]

expected_results = [
    True,
    True,
    True,
    False
]

for example, result in zip(examples, expected_results):
    if s.backspaceCompare(example[0], example[1]) == result:
        print("Correct!")
    else:
        print("Incorrect answer for ", example)