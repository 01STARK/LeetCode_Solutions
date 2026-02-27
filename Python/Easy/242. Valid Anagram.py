class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        boolean = False
        for i in s:
            if t.count(i) == s.count(i) and len(s)==len(t):
                boolean = True
            else:
                boolean = False
                break
        return boolean
