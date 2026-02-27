# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         start, end = -1, -1
    
#         l= 0
#         r = len(nums) - 1
        
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] >= target:
#                 if nums[mid] == target:
#                     start = mid
#                 r = mid - 1 
#             else:
#                 l = mid + 1

#         l= 0
#         r = len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] <= target:
#                 if nums[mid] == target:
#                     end = mid
#                 l = mid + 1 
#             else:
#                 r = mid - 1
                
#         return [start, end]
                    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0,0
        while r<len(nums) and nums[r] !=target:
            r+=1

        if r == len(nums):
            return [-1,-1]
        l =r
        while r < len(nums) and nums[r] == target :
            r+=1
        return [l, r-1]
     
        
