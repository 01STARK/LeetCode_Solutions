class Solution:
    def maxSumSubarrays(self, nums, k):
        n=len(nums)
        window_sum=sum(nums[:k])
        big=window_sum
        for i in range(1,n-k+1):
            j=i+k-1
            window_sum=window_sum-nums[i-1]+nums[j]
            if big<(window_sum):
                big=window_sum     
        return big
            
so=Solution()
nums = [2, 3, 4, 1, 5]; k = 2
print(so.maxSumSubarrays(nums,k))