class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)

        for idx in range(n-1):
            if nums[idx] !=idx+1:
                return False
        return nums[-1] == n - 1