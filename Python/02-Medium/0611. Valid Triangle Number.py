class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #a+b>c
        sort=sorted(nums)
        n=len(sort)
        count=0
        for i in range(n-1,1,-1):
            l=0
            r=i-1
            while l<r:
                if sort[l]+sort[r]>sort[i]:
                    count+=r-l
                    r-=1
                else:
                    l+=1
        return count
