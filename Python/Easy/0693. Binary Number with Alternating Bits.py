class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary=bin(n)[2:]
        flag=True
        if len(binary)<2:
            return flag
        for i in range(len(binary)-1):
            if binary[i]==binary[i+1]:
                return False
        return flag
