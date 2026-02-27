from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen=[]
        idx=0
        count=0
        while idx<n:
            ele=s[idx]
            if ele in seen:
                seen.append(ele)
                count=max(count,len(seen))
            else:
                count=max(count,len(seen))
                seen=seen[(seen.index(ele))+1:]
                seen.append(s[idx])
            idx+=1
        return count
        
        
