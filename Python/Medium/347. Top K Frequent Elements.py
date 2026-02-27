import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap=[]
        freq_map=defaultdict(int)

        for num in nums:
            freq_map[num]+=1

        for num,freq in freq_map.items():
            heapq.heappush(min_heap,(freq,num))

            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [freq for num,freq in sorted(min_heap,reverse=True)]
