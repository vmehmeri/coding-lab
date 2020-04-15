from typing import List

# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return None
        
        triplets = []
        
        nums.sort()
        N = len(nums)
        
        for i in range(N-2):
            if nums[i] > 0: 
                break
                
            # Skip repeated numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i+1, N-1
            
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    triplets.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                        
                    l+=1
                    r-=1
                    continue
                elif total > 0:
                    r-=1
                else:
                    l+=1
                    
        return triplets

nums = [-1, 0, 1, 2, -1, -4]

s = Solution()
print(s.threeSum(nums))