class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest=float('inf')
        sorted_nums=sorted(nums)
        for i in range(len(sorted_nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                total = sorted_nums[i]+sorted_nums[l]+sorted_nums[r]
                if abs(target-total)<abs(target-closest):
                    closest=total
                if total<target:
                    l+=1
                elif total>target:
                    r-=1
                else:
                    break
        return closest