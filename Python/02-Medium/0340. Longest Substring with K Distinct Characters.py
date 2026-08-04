from collections import defaultdict


class Solution:
    def longestSubstringWithKDistinct(self, s, k):
        n=len(s)
        mapit=defaultdict(int)
        count=0
        l,r=0,0
        while r < n:
            mapit[s[r]] += 1

            while len(mapit) > k:
                mapit[s[l]] -= 1
                if mapit[s[l]] == 0:
                    del mapit[s[l]]
                l += 1

            count = max(count, r - l + 1)
            r += 1
        return count
so=Solution()
s = "abcadcacacaca"; k = 3
#    0123456789
print(so.longestSubstringWithKDistinct(s,k))