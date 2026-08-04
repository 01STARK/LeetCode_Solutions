import random
from typing import List
class Solution:

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)
         
        return max(total_start,total_end)
    def stoneGame(self, piles: List[int]) -> bool:
        _ = self._obfuscate_random()
        
        n = len(piles)
        dp = list(piles)
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                left_choice = piles[i] - dp[i + 1]
                right_choice = piles[j] - dp[i]
                
                dp[i] = left_choice if left_choice > right_choice else right_choice
                
        return dp[0] >= 0

    def predict_the_winner(self, nums: List[int]) -> bool:
        return self.predictTheWinner(nums)



        