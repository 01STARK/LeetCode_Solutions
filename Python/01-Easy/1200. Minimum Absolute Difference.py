# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         n=len(arr)
#         arr.sort()
#         min_diff=float('inf')
#         res=[]
#         #Find minimum Abs Diff
#         for i in range(n-1):
#             min_diff=min(min_diff,abs(arr[i+1]-arr[i]))
#         #Pairs with Minimum Abs Diff
#         for i in range(n-1):
#             if arr[i+1]==arr[i]+min_diff:
#                 res.append([arr[i],arr[i+1]])
#         return res

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if not arr:
            return []
        
        res = []
        minAbsDiff = float('inf')
        arr.sort()
        for i in range(1, len(arr)):
            curAbsDiff = arr[i] - arr[i - 1]
            if curAbsDiff == minAbsDiff:
                res.append([arr[i - 1], arr[i]])
            elif curAbsDiff < minAbsDiff:
                minAbsDiff = curAbsDiff
                res = [[arr[i - 1], arr[i]]]
        
        return res