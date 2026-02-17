class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        seen = set()
        for i in range(n):
            seen.clear()
            balance = 0
            if res > n - i:
                break
            for j in range(i, n):
                num = nums[j]
                if num not in seen: 
                    if num % 2:
                        balance -= 1
                    else:
                        balance += 1
                    seen.add(num)
                if balance == 0:
                    res = max(res, j - i + 1)
        
        return res
                