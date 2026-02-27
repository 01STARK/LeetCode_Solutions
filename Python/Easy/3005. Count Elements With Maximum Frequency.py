from collections import defaultdict
import heapq
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # n=len(nums)
        # freq=defaultdict(int)
        # heap=[]
        # for i in n:
        #     freq[i]+=1
        # for num,freq in freq.items():
        #     heapq.heappush(heap,(freq,num))
        # maxi= num for num,freq in sort(heap,reverse=True)
        # print(maxi) 
    
    # DONE
        c = {}

        for i in nums:
            c[i]=nums.count(i)

        max_freq = max(c.values())
        same_count =0
        for _,val in c.items():
            if val==max_freq:
                same_count+=1

        return (max_freq*same_count)
