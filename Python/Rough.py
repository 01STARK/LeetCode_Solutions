class Solution:
    def minRemoval(self, nums, k) -> int:
        n=len(nums)
        nums.sort()
        op_count=0
        l=0
        updated_len=0
        for r in range(n):
            while nums[r]>nums[l]*k:
                l+=1
            updated_len=max(updated_len,r-l+1)
            op_count=n-updated_len
        return op_count

nums=[1,6,4,2,9]
#nums=[10,30,11]
k=3
so=Solution()
print(so.minRemoval(nums,k))



# maximum_num,minimum_num=max(nums),min(nums)
#             # max <= min * k
#             if maximum_num<=minimum_num*k:
#                 sol=False
#                 break
#             if len(nums)>1:
#                 if maximum_num>(minimum_num*k*2):
#                     nums.remove(maximum_num)
#                     op_count+=1
#                 else:
#                     nums.remove(minimum_num)
#                     op_count+=1
#             else:
#                 sol=False