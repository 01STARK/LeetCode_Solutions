class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n=len(nums)
        state=0
        
        for i in range(n-1):
            if state==0:
                if nums[i+1]>nums[i]:
                    continue
                elif nums[i]>nums[i+1] and i>0:
                    state=1
                else:
                    return False
            elif state==1:
                if nums[i+1]<nums[i]:
                    continue
                elif nums[i+1]>nums[i]:
                    state=2
                else: return False
            else:
                if nums[i+1]>nums[i]:
                    continue
                else:
                    return False
        return state==2