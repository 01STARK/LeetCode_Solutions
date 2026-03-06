class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0
        def col_sum(col_idx):
            return sum(row[col_idx] for row in mat)
        
        for row in mat:
            if sum(row)==1:
                col_idx=row.index(1)
                count += col_sum(col_idx)==1
        return count