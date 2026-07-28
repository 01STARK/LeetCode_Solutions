class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num=list(set(nums))
        num.sort()
        print(num)
        if len(num)<3:
            return num[-1]
        return num[-3]