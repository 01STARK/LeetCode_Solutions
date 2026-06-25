class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        j=0
        seen=set()
        max_len=0
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[j])
                j+=1
            seen.add(s[i])
            max_len=max(max_len,i-j+1)
        return max_len