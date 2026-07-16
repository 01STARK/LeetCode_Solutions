class Solution:
    def countMajoritySubarrays(self, nums, target):
        n=len(nums)
        count=0
        for i in range(n):
            for j in range(i+1,n+1):
                sub=nums[i:j]
                #print(sub.count(target))
                if sub.count(target)>len(sub)//2:
                    count+=1
        return count

so=Solution()
nums =[1,1,1,1]
target =1
print(so.countMajoritySubarrays(nums,target))
