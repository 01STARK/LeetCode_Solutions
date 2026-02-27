# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         longest=''
#         for i in range(len(s)):
#             for j in range(i+1,len(s)+1):
#                 substr=s[i:j]
#                 rev=substr[::-1]
#                 if rev==substr and j-i+1>len(longest):
#                     longest=substr
#         return longest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        longest=''
        if not s:
            return ''
        def wings(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(n):
            longest=max(wings(i,i),wings(i,i+1),longest,key=len)
        return longest
