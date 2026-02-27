def maxSumTrionic(nums):
    # state=0 ---0 to l   - not sure
    # state=1 ---l to p   - increasing
    # state=2 ---p to q   - decreasing
    # state=3 ---q to r   - increasing
    # state=4 ---r to n-1 - not sure
    n=len(nums)
    state=0
    start=0
    stop=0
    l=None
    p=0
    q=0
    r=0
    total=[]
    for i in range(0,n):
        # [0,-2,-1,-3,0,2,-1]
        if state==0: #not sure state
            # if nums[i+1]>=nums[i]:
            #     continue
            if i==0 and nums[i]<nums[i+1]:
                start=i
                if l==None:
                    l=i
                print('l ',l)
                state=1
            if nums[i-1]<nums[i]:
                start=i-1
                l=i-1
                print('l ',l)
                state=1
            else:
                continue
        elif state==1:# Increasing State
            if nums[i]>nums[i-1]:
                continue
            elif nums[i]<nums[i-1]:
                state=2
                p=i-1
                print('p ',p)
            else:
                state=0
                l=i
        elif state==2: # Decreasing State
            if nums[i]<nums[i-1]:
                continue
            elif nums[i]>nums[i-1]:
                state=3
                q=i-1
                print('q ',q)
            else:
                state=0
        elif state==3: #Increasing State
            if i!=n-1:
                if nums[i]>nums[i-1]:
                    continue
                elif nums[i]<=nums[i-1]:
                    stop=i-1
                    state=4
                    r=i-1
                    print('r ',r)
                else:
                    state=0
            elif nums[i]>=nums[i-1]:
                stop=i-1
                state=4
                r=i
                #print('r ',r)
        if state==4:
            state=0
            addition=sum(nums[start:stop+1])
            #print('Sum ',addition)
            total.append(addition)
    
    return max(total)
#nums =[0,-2,-1,-3,0,2,-1]
#nums = [1,4,2,7]
nums=[1,4,2,2,3,1,2]
print(maxSumTrionic(nums))