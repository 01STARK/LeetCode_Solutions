class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty=customers.count('Y')
        min_penalty=penalty
        hour=0
        for i,r in enumerate(customers):
            if r=='Y':
                penalty-=1
            else:
                penalty+=1
            if penalty<min_penalty:
                penalty=min_penalty
                hour = i+1

        return hour