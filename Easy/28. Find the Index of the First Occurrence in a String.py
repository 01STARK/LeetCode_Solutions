class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        if len(haystack)>=len(needle) and needle in haystack:
            index = haystack.find(needle)
            return index
        else:
            return -1