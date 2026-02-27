class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ''
        for i in digits:
            st = st+str(i)
        output = []
        num = int(st)+1
        st = str(num)
        
        for i in st:
            output.append(int(i))
        
        return output
