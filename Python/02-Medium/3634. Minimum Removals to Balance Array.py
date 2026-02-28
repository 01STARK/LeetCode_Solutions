class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
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