class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        neg=False
        num=0
        if len(s)<1:
            return 0
        if s[0]=='+' or s[0]=='-':
            if s[0]=='-':
                neg=True
            s=s[1:]
        #s=s.lstrip('0')
        for i in range(len(s)):
            if not s[i].isdigit():
                s=s[:i]
                break
            else:
                continue
        if len(s)>0:
            if neg:
                num=int(s)*-1
            else: 
                num = int(s)
            if num < -(2**31):
                return -(2**31)
            elif num >(2**31)-1:
                return (2**31)-1
            else:
                return num
        else:
            return num 
