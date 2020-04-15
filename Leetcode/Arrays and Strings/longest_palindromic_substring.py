# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return s

        # Dictionary to store palindrome computations
        _isPalindromeResults = {}

        def _isPalindrome(s, start, end):
            l = start
            r = end

            ## if substring in the "middle" is palindrome, this 
            ## will be a palindrome too if the outer characters match
            ## Saves computation time.
            if (l+1,r-1) in _isPalindromeResults and _isPalindromeResults[(l+1,r-1)] == True and s[l] == s[r]:
                _isPalindromeResults[(l,r)] = True
                return True

            while l<r:
                if s[l] != s[r]:
                    _isPalindromeResults[(l,r)] = False
                    return False
                else:
                    l+=1
                    r-=1
                    if (l+1,r-1) in _isPalindromeResults and _isPalindromeResults[(l+1,r-1)] == True and s[l] == s[r]:
                        _isPalindromeResults[(l,r)] = True
                        return True

            _isPalindromeResults[(l,r)] = True
            
            return True

        
        longest = (0,0)
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if _isPalindrome(s, i, j) and (j-i) > longest[1]-longest[0]:
                        longest = (i,j)
                
               
        
        return s[longest[0]:longest[1]+1]

s = Solution()

print(s.longestPalindrome("aacdefcaa"))
print(s.longestPalindrome("fffufff"))