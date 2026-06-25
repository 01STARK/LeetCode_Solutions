class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n=len(mat[0])
        k=k%n
        for i,row in enumerate(mat):
            # direction
            direction=-k if i%2!=0 else k
            for c in range(n):
                if row[c] != row[(c+direction)%n]:
                    return False
        return True