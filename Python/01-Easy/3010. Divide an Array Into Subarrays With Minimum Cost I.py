class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # min1 = float('inf')
        # min2 = float('inf')

        # for num in nums[1:]:
        #     if num < min1:
        #         min2 = min1
        #         min1 = num
        #     elif num < min2:
        #         min2 = num

        # return nums[0] + min1 + min2
        num_sort=sorted(nums[1:])
        return nums[0]+num_sort[0]+num_sort[1]