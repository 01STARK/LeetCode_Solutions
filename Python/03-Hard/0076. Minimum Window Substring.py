class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for c in t:
            d[c]+=1
        formed_word,total =0,len(d)
        l,r=0,0
        ans_len = float('inf')
        subl,subr = 0,0
        s_len = len(s)
        while r<s_len:
            c = s[r]
            if c in d:
                d[c]-=1
                if d[c]==0:#char formed
                    formed_word+=1
            while l<=r and formed_word ==total:
                cur_len = r-l+1
                if cur_len < ans_len:
                    ans_len = cur_len
                    subl,subr=l,(r+1)
                c =s[l]
                if c in d:
                    if d[c]==0:
                        formed_word -=1
                    d[c] +=1
                l +=1
            r+=1
        if ans_len == float('inf'):
            return ""
        else:
            return s[subl:subr]