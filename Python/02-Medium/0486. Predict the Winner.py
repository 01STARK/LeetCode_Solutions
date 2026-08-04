class Solution:
   
    
    def totalScore(self,nums,s,e):
        # base case
        if s==e:
            return nums[s]
        
        # Choose start
        total_start =  nums[s] - self.totalScore(nums,s+1,e)
        
        # Choose end
        total_end =  nums[e] - self.totalScore(nums,s,e-1)
        
        return max(total_start,total_end)
     
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        s = self.totalScore(nums,0,n-1)
        
        if s>=0:
            return True
        return False
        