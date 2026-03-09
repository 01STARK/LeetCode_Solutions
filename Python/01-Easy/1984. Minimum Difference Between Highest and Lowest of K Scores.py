class Solution:
    def minimumDifference(self, nums, k):
        if k<2:
            return 0
        diff=float('inf')
        n=len(nums)
        l=0
        r=l+k
        nums.sort()
        for i in range(n-k+1):
            max_sub,min_sub=nums[i+k-1],nums[i]
            temp_diff=max_sub-min_sub
            diff=min(diff,temp_diff)
        return diff

#Approch 2(same trick less lOC)
# class Solution:
#     def minimumDifference(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         nums.sort()
#         return min(nums[i+k-1]-nums[i] for i in range(n-k+1))