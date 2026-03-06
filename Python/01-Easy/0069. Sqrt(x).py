class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x//2
        if x==1:
            return x
        while l<=r:
            mid=(l+r)//2
            sqr=mid*mid  
            if sqr==x:
                return mid
            elif sqr<x:
                l=mid+1
            else:
                r=mid-1
        return r
        
    
        # if x < 2:
        #     return x
    
        # g = x
        # while g * g > x:
        #     g = (g + x // g) // 2
        
        # return g

# f(g) = g**2 - x
# f'(g) = 2g

# newton rule gn+1 = g_n - f(g_n)/f'(g_n)

# = gn - (g**2 - x)/(2g)
# gn+1= gn - (g/2 - x/2g)
# = g/2+x/2g = (g+x//g)//2