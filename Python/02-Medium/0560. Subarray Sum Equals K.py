class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n=len(nums)
        # count=0
        # for i in range(n-1):
        #     j=i+1
        #     tot=nums[i]
        #     if nums[i]==k:
        #         count+=1
        #     while j<n:
        #         if tot+nums[j]==k:
        #             count+=1
        #         tot=tot+nums[j]
        #         j+=1
        # if nums[-1]==k:
        #     count+=1
            
        # return count
        
        # prefix_sum_count=Counter({0:1})
        # result=0
        # curr_sum=0
        # for num in nums:
        #     curr_sum +=num
        #     result+=prefix_sum_count[curr_sum-k]
        #     prefix_sum_count[curr_sum]+=1
        # return result
        
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res