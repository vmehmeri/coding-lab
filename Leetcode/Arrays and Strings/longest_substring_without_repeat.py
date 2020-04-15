# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or s == "":
            return 0
        if len(s) == 1:
            return 1

        char_map = {}
        max_len = 0
        current_len = 0
        current_start = 0

        for pos,c in enumerate(s):
            if c not in char_map or char_map[c] < current_start:
                current_len += 1
                max_len = max(max_len, current_len)
                char_map[c] = pos
            else:
                # Letter occurred before. Update max len
                max_len = max(max_len, current_len)
                current_start = char_map[c] + 1
                current_len = pos - current_start + 1
                char_map[c] = pos
        
        return max_len

print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("au"))