class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        count=0
        if n<9: return n
        total=n
        for i in range(1,(n//8)+2):
            if total>=8:
                count+=8*i
                total-=8  
            else:
                count+=(total*i)
        return count