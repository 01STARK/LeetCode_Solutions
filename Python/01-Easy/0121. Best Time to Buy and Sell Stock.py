class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_prof=0
        for price in prices[1:]:
            if min_price>price:
                min_price=price
            else:
                if max_prof<price-min_price:
                    max_prof=price-min_price
        return max_prof