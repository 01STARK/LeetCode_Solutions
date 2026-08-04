class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s1=len(s)
        p1=len(p)
        if s1<p1:
            return []
        result=[]
        cs=[0]*26
        cp=[0]*26
        for i in range(p1):
            cs[ord(s[i])-97]+=1
            cp[ord(p[i])-97]+=1
        if cs==cp:
            result.append(0)
                
        for i in range(p1,s1):
            cs[ord(s[i])-97]+=1
            cs[ord(s[i-p1])-97]-=1
            if cs==cp:
                result.append(i-p1+1)
        return result