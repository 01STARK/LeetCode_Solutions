class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # n =len(fruits)
        # used_bskt =[False]*n
        # unplaced_counts=0
        
        # for f in fruits:#0,1,2
        #     placed=False
        #     for i in range(n):
        #         if not used_bskt[i] and baskets[i] >= f:
        #             used_bskt[i]=True
        #             placed =True
        #             break
        #     if not placed:
        #         unplaced_counts+=1
        # return unplaced_counts
        result = len(fruits)
        for fruit in fruits:
            for basket in baskets:
                if basket>=fruit:
                    result-=1
                    baskets.remove(basket)
                    break
        return result
