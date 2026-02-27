class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # n=len(arr)
        # binary_list={}

        # if n==1:
        #     return arr
        
        # for i in range(n):
        #     binary_list[i]=[arr[i],bin(arr[i]).count('1')]
        # values = binary_list.values()
        
        # ordered_indexes = [x[0] for x in sorted(values, key=lambda x: x[1])]
        
        # return (ordered_indexes)


        #APPROACH 2
       # return sorted(arr, key=lambda x: (bin(x).count('1'), x))

       #APPROACH 3
        # arr.sort(key=lambda num : (num.bit_count(),num))
        # return arr

        #APPROACH 4
        h = {}
        
        for a in arr:
            c = a.bit_count()
            if c in h:
                h[c].append(a)
            else:
                h[c] = [a]
        
        ans = []
        
        for c in sorted(h.keys()):
            ans.extend(sorted(h[c]))
        
        return ans