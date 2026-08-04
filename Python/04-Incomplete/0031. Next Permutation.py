class Solution:
    def nextPermutation(self, nums):
        n=len(nums)
        i=n-2
        while i>=0 and nums[i] >=nums[i+1]:
            i-=1
            
        imp=i
        if i>=0:
            j=n-1
            while nums[j]<=nums[i]