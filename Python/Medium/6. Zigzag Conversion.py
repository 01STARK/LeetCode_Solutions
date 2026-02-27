class Solution:
    def convert(self, s: str, numRows: int) -> str:                
    # Empty list
        res=''
        rows = [''] * numRows
        index = 0
        step = 1
        if numRows==1:
            return s
            
    # Iterate over all characters 
        for char in s:
            rows[index] += char
            # print(rows)
            # Update the index and direction
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1    
            index += step
        # print(rows)
        for i in rows:
            res=res+str(i)
        return res