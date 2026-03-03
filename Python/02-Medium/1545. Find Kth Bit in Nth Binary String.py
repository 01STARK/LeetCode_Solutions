class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Brute Force Approch
        #------------------------
        # s='0'
        # def reverse_invert(s):
        #     rev=''
        #     if len(s)<2:
        #         return '1'
        #     for i in range(len(s)-1,-1,-1):
        #         if s[i]=='0':
        #             rev+='1'
        #         else:
        #             rev+='0'
        #     return rev
        # for i in range(n-1):
        #     rev=reverse_invert(s)
        #     s=s+'1'+rev
        # return s[k-1]
        
        # Efficient Approach:
        if n == 1:
            return "0"
        
        mid = 1 << (n - 1)
        if k == mid:
            return "1"
        
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        mirrored = (1 << n) - k
        bit = self.findKthBit(n - 1, mirrored)
        return "1" if bit == "0" else "0"