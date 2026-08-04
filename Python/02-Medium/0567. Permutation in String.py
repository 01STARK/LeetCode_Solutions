class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # n1,n2=len(s1),len(s2)
        # m1={}
        # if n1>n2:
        #     return False
        # for i in s1:
        #     m1[i]=m1.get(i,0)+1
        
        # for i in range(n2):
        #     j=i+n1
        #     m2={}
        #     for k in s2[i:j]:
        #         m2[k]=m2.get(k,0)+1
        #     if m1==m2:
        #         return True
        # return False
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - 97] += 1
            window_count[ord(s2[i]) - 97] += 1

        if s1_count == window_count:
            return True

        for i in range(len(s1), len(s2)):
             window_count[ord(s2[i]) - 97] += 1
             window_count[ord(s2[i - len(s1)]) - 97] -= 1

             if s1_count == window_count:
                return True