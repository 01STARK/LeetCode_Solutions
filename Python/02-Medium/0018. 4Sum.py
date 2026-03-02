class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicate for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = n - 1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total > target:
                        l -= 1
                    elif total < target:
                        k += 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        # Skip duplicates for k and l
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        # while k < l and nums[l] == nums[l - 1]:
                        #     l -= 1
                        k += 1
                        # l -= 1

        return ans