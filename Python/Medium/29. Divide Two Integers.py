class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_limit = - (2**31)
        max_limit =  (2**31) -1

        if dividend ==min_limit and divisor==-1:
            return max_limit
        
        a,b = abs(dividend),abs(divisor)
        quotient = 0
        is_neg = False
        # both has different sign then neg
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            is_neg = True
 
        max_shift = 0
        while a >= (b << (max_shift + 1)):
            max_shift += 1

        # print(max_shift) # 3>>1 = 6  

        for i in range(max_shift, -1, -1):
            if a >= (b << i):
                a -= (b << i)
                quotient += (1 << i)
        
        if is_neg:
            return -quotient
        else:
            return quotient