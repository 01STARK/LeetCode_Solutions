class Solution:
    def minSwaps(self, grid):
        # grid[0][1] grid[0][2]
        #            grid[1][2]
        # n=len(grid)
        # count=0
        # for i in range(n):
        #     for j in range(1,n):
        #         if grid[i][1:].count(0)==n-j:
        #             if i==j-1:
        #                 grid[i],grid[j-1]=grid[j-1],grid[i]
        #             else:
        #                 grid[i],grid[j-1]=grid[j-1],grid[i]
        #                 count+=1 
        # return count
        
        # 1. Count trailing zeros for each row
        # 2. For each position i, find the first available row that satisfies the condition
            # Look for a row from i onwards that has enough zeros
            # If no such row is found, it's impossible
        # 3. Bubble the found row up to position i
            # Each step in the bubble is one swap
            return grid
        
so=Solution()
grid =[[0,0,1],[1,1,0],[1,0,0]]
print(so.minSwaps(grid))