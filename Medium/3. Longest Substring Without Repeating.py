class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        maxi=0
        k=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[k])
                k+=1
            seen.add(s[i])
            
            maxi=max(maxi,len(s[k:i])+1)
        return maxi
