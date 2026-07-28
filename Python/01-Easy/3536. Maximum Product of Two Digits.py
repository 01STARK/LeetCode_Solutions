# class Solution:
#     def maxProduct(self, n: int) -> int:
#         list1=[int(d) for d in str(n)]
#         list1.sort()
#         return list1[-1]*list1[-2]

class Solution:
    def maxProduct(self, n: int) -> int:
        max_val = n % 10
        sec_max = -1
        n //= 10
        
        while n > 0:
            digit = n % 10
            if digit < max_val:
                sec_max = max(sec_max, digit)
            elif digit == max_val:
                sec_max = max_val
            else:
                sec_max = max_val
                max_val = digit
            n //= 10
            
        return max_val * sec_max