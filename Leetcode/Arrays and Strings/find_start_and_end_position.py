from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        self.start = self.end = -1
        
        def binarySearchStart(nums,target,i,j):
            if j < i:
                return
            
            middle = (i+j)//2
            if nums[middle] == target and (middle == 0 or nums[middle-1] != target):
                self.start = middle
                return
            else:
                if nums[middle] < target:
                    binarySearchStart(nums,target,middle+1,j)
                else:
                    binarySearchStart(nums,target,i,middle-1)
                    
        def binarySearchEnd(nums,target,i,j):
            if j < i:
                return
            
            middle = (i+j)//2
            if nums[middle] == target and (middle == len(nums)-1 or nums[middle+1] != target):
                self.end = middle
                return
            else:
                if nums[middle] > target:
                    binarySearchEnd(nums,target,i,middle-1)
                else:
                    binarySearchEnd(nums,target,middle+1,j)
                    
        binarySearchStart(nums,target,0,len(nums)-1)
        if self.start == -1:
            return [-1,-1]

        binarySearchEnd(nums,target, self.start,len(nums)-1)
        
        if self.start == -1 and self.end != -1:
            self.start = self.end
        elif self.end == -1 and self.start != -1:
            self.end = self.start
            
        return [self.start,self.end]

s = Solution()
example = [5,7,7,8,8,10]

print(
    s.searchRange(example, 8)
)