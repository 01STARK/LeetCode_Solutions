class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        first_group=0
        second_group=1
        for i in range(1,n):
            if s[i]==s[i-1]:
                second_group+=1
            else:
                count+=min(first_group,second_group)
                first_group=second_group
                second_group=1
        count+=min(first_group,second_group)
        return count
                    