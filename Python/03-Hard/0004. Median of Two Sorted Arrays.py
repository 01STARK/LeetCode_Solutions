class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list3=sorted(nums1+nums2)
        n= len(list3)
        if n%2==0:
            answer=(list3[int(n/2)]+list3[int(n/2)-1])/2
        else:
            answer=(list3[n//2])
        return answer