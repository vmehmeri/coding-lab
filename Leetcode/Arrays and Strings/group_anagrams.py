# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

from typing import List
from collections import Counter
# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.
#

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def _isAnagram(a, b):
            return Counter(a) == Counter(b) 

        anagrams = []
        for s in strs:
            found = False
            for anag in anagrams:
                if _isAnagram(s, anag[0]):
                    anag.append(s)
                    found = True
                    break
            
            if not found:
                anagrams.append([s])

        return anagrams

example = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(example))