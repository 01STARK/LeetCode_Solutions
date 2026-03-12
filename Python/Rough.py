import itertools
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = (10**9) + 7
        def dp(z,o,last,count):
            if z == 0 and o == 0:
                return 1
            ans = 0

            if z > 0:
                if last != 0:
                    ans += dp(z-1, o, 0, 1)
                elif count < limit:
                    ans += dp(z-1, o, 0, count+1)

            if o > 0:
                if last != 1:
                    ans += dp(z, o-1, 1, 1)
                elif count < limit:
                    ans += dp(z, o-1, 1, count+1)

            return ans % MOD
so=Solution()
print(so.numberOfStableArrays(3,3,2))