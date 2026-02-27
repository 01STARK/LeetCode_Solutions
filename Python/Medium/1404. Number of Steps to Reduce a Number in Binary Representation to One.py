class Solution:
    def numSteps(self, s: str) -> int:
        s=int(s,2)
        print(s)
        count=0
        while s>1:
            if s%2!=0:
                s=s+1
                count+=1
            else:
                count+=1
                s=int(s//2)
        return count                