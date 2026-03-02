class Solution:
    def minPartitions(self, n: str) -> int:
        # Approach 1
        # total=0
        # og_n=n[:]
        # count=0
        # while str(total)!=og_n:
        #     temp=''
        #     for i in range(len(n)):
        #         if n[i]!='0':
        #             temp=temp+'1'
        #         else:
        #             temp=temp+'0'
        #     n=str(int(n)-int(temp))
        #     total=int(total)+int(temp)
        #     count+=1
        # return count

        # Approach 2
        # return int(max(n))

        # Approach 3
        for i in "987654321":
            if i in n:
                return int(i)