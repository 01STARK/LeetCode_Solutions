class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        #make number
        for i in range(1,9):
            a=i
            for j in range(i+1,10):
                a=a*10+j
                if low<=a<=high:
                    res.append(a)
        return sorted(res)
