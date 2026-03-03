class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 1. Count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        swaps = 0
        # 2. For each position i, find the first available row that satisfies the condition
        for i in range(n):
            target_required = n - 1 - i
            found_idx = -1
            
            # Look for a row from i onwards that has enough zeros
            for j in range(i, n):
                if trailing_zeros[j] >= target_required:
                    found_idx = j
                    break
            
            # If no such row is found, it's impossible
            if found_idx == -1:
                return -1
            
            # 3. Bubble the found row up to position i
            # Each step in the bubble is one swap
            while found_idx > i:
                trailing_zeros[found_idx], trailing_zeros[found_idx - 1] = \
                    trailing_zeros[found_idx - 1], trailing_zeros[found_idx]
                swaps += 1
                found_idx -= 1
                
        return swaps