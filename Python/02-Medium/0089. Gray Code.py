class Solution:
    def grayCode(self, n: int) -> List[int]:
         # first number: 0
        result = [0]
    
    # addinh 'n' bits total
        for i in range(n):
            # 1 << i = 2**i
            add_bit = 1 << i
        
        # current list, reverse it, and add 'add_bit' to each
            mirrored_part = []
            for x in reversed(result):
                mirrored_part.append(x + add_bit)
            
            # Combine the original list with our new mirrored part
            result.extend(mirrored_part)
        
        return result