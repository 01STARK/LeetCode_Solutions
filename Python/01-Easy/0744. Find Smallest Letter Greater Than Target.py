class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo, hi = 0, len(letters)
        while lo < hi:
            mid = (lo + hi) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return letters[lo % len(letters)]
        
        # smallest=None
        # for i in letters:
        #     if i>target and (smallest== None or i < smallest): 
        #         smallest=i
        # return smallest if smallest else letters[0]