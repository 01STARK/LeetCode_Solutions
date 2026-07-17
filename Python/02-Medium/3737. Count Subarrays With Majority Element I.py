class Solution:
#     def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
#         n=len(nums)
#         count=0
#         for i in range(n):
#             t_count=0
#             leng = 0
#             for j in range(i,n):
#                 leng+=1
#                 if nums[j]==target:
#                     t_count+=1
#                 if t_count>leng//2:
#                     count+=1
#         return count

    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return 0

        count = 0
        fromLeft = [count := count + (1 if val == target else 0) for val in nums]

        ans = 0
        n = len(nums)

        for i in range(n):
            toi = fromLeft[i]

            startj = 0
            intervalTargets = toi

            while True:
                startj = max(startj, i - intervalTargets * 2 + 1)
                toj = fromLeft[startj - 1] if startj > 0 else 0
                if intervalTargets == toi - toj:
                    break
                intervalTargets = toi - toj


            length = i + 1 - startj
            for j in range(startj, i + 1):
                nbTargets = toi - toj
                ans += nbTargets * 2 > length
                length -= 1

                toj = fromLeft[j]

        return ans