
from collections import defaultdict
class Solution:
    def longestBalanced(self, s):
        n=len(s)
        balanced_substring=set()
        
        l=0
        r=1
        while l<n:
            di=defaultdict(int)
            s_set=s[l:r+1]
            count_a=0
            count_b=0
            count_c=0
            for i in s[l:r+1]:
                #print(i)
                if i=='a':
                    count_a+=1
                if i=='b':
                    count_b+=1
                if i=='c':
                    count_c+=1
            if count_a!=0:
                di['a']=count_a
            if count_b!=0:
                di['b']=count_b
            if count_c!=0:
                di['c']=count_c
            if len(set(di.values()))==1:
                balanced_substring.add(len(s[l:r+1]))
            if r<n:
                r+=1
            if r>=n:
                l+=1
                r=l+1
            #print(balanced_substring)
        if balanced_substring:
            return max(balanced_substring)
        else:
            return 0
so=Solution()
s='accc'
print(so.longestBalanced(s))