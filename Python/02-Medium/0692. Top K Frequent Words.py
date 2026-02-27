from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k):
        freq = Counter(words)
        #print(freq)
        heap = []
        
        for word in freq:
            heapq.heappush(heap, (-freq[word], word))
        print(heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
            print(result)
        
        return result
