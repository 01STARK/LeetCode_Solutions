class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxi=nums[0]
        curr_max=nums[0]
       
        for i in nums[1:]:
            curr_max=max(i,curr_max + i)
            maxi=max(maxi,curr_max)
        return maxi