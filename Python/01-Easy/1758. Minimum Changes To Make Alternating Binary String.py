class Solution:
    def minOperations(self, s: str) -> int:
        # n=len(s)
        # count1=0
        # count2=0       
        # s1=list(s)
        # s2=s1.copy()
        # for i in range(n):
        #     if i%2==0 and s1[i]!='0':
        #         s1[i]='0'
        #         count1+=1
        #     elif i%2!=0 and s1[i]!='1':
        #         s1[i]='1'
        #         count1+=1
        # for i in range(n):
        #     if i%2==0 and s2[i]!='1':
        #         s2[i]='1'
        #         count2+=1
        #     elif i%2!=0 and s2[i]!='0':
        #         s2[i]='0'
        #         count2+=1  
        
        # return min(count1,count2)
        n=len(s)
        count = 0
        for i in range(n):
            if s[i] != ("1" if i % 2 == 0 else '0'):
                count += 1
        return min(count, n - count)