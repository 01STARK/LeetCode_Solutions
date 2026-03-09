class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        for i in range(n+1):
            binary=bin(i)[2:].zfill(n)
            if binary not in nums:
                return binary
        
        # n = len(nums)
        # res = []
        # for i in range(n):
        #     current_str = nums[i]
        #     char = current_str[i]
            
        #     if char=="0":
        #         res.append("1")
        #     else:
        #         res.append("0")
        #     print("res for",i,"is ",res)
        # return "".join(res) 