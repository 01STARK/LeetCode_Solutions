class Solution:
    def reverseBits(self, n: int) -> int:
        # binary=format(n,'032b')
        # revBin=binary[::-1]
        # return int(revBin,2)
        return int(bin(n)[2:].zfill(32)[::-1], 2)
