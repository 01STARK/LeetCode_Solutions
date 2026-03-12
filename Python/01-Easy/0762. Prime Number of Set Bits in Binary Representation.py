class Solution:
    def is_prime(self,n):
        if n <= 1:
            return False
        if n<=3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False  
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6 #6k ± 1
        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        for i in range(left,right+1):
            ones=i.bit_count()
            if self.is_prime(ones):
                count+=1
        
        return count

# Approach 2
# class Solution:

#     def countPrimeSetBits(self, left: int, right: int) -> int:
#         count=0
#         for i in range(left,right+1):
#             ones=i.bit_count()
#             if ones in [2, 3, 5, 7, 11, 13, 17,19]:
#                 count+= 1  
#         return count