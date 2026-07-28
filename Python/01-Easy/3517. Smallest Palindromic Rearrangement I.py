class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return s
        if n%2==0:
            front=s[:(n//2)]
            mid=''
        else:
            front=s[:(n//2)]
            mid=s[(n//2)]
        return "".join(sorted(front))+mid+"".join(sorted(front,reverse=True))