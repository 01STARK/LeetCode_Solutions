class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)
    
        total = 0
        for i in range(k):
            current_happiness = (happiness[i] - i) if (happiness[i] - i) >0 else 0
            if current_happiness == 0:
                break
            
            total += current_happiness
        return total
        # ----------------------------------------
        # max_happiness = 0
        # happiness.sort(reverse=True)

        # i = 0
        # while k !=0 :
        #     happiness_value = happiness[i] - i
        #     if happiness_value <= 0 :
        #         break
        #     max_happiness += happiness_value
        #     i += 1
        #     k -= 1

        # return max_happiness
        
        
        # arr=sorted(happiness,reverse=True)
        # #print(arr)
        # total=0
        # count=0
        # while len(arr)!=0 and k!=0:
        #     #print(arr[0])
        #     if len(arr)<1:
        #         break
        #     else:
        #         total=total+arr[0]
        #         arr=arr[1:]
        #         count+=1
        #         # arr[0]=arr[0]-1
        #         # if arr[0]<0:
        #         #     arr=arr[1:]
        #         arr = [x - 1 for x in arr if x - 1 != 0]
        #         k-=1
        # return total

       