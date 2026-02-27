class Solution:
    def addBinary(self, a: str, b: str) -> str:
        inta=int(a,2)
        intb=int(b,2)
        tot=inta+intb
        print(tot)
        return format(tot,'b')