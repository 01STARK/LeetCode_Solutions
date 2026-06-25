class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag=True
        new_s= ''.join(c.lower() for c in s if c.isalnum())
        l=0
        r=len(new_s)-1
        while l<r:
            if new_s[l]!=new_s[r]:
                flag=False
            l+=1
            r-=1
        return flag