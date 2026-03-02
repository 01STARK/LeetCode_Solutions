class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        rev=0
        
        if x==0:
            return 0
        if x<0:
            sign = -1
            x=-x
        rev=int(str(x)[::-1])
        rev*=sign
        if (-2**31)<rev and rev<(2**31 -1):
            return rev
        else: return 0