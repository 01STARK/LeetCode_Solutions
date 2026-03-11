class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary=bin(n)[2:]
        res_binary=''
        for i in binary:
            if i=='1':
                res_binary+='0'
            elif i=='0':
                res_binary+='1'
        #print(res_binary)
        return int(res_binary,2)