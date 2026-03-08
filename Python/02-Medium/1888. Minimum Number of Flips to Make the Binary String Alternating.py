class Solution:
    def minFlips(self, s: str) -> int:
        n=len(s)
        s=s+s
        sam1 = ""
        sam2 = ""
        count=float('inf')
        # Making samples
        for i in range(len(s)):
            if i % 2 == 0:
                sam1 += "0"
                sam2 += "1"
            else:
                sam1 += "1"
                sam2 += "0"
        
        diff1 = diff2 = 0
        l = 0
        
        # Comparing with samples
        for r in range(len(s)):
            if s[r] != sam1[r]:
                diff1 += 1
            if s[r] != sam2[r]:
                diff2 += 1
            # Rotate string
            if r - l + 1 > n:
                if s[l] != sam1[l]:
                    diff1 -= 1
                if s[l] != sam2[l]:
                    diff2 -= 1
                l += 1
            if r - l + 1 == n:
                count = min(count, diff1, diff2)
        return count