def maxArea(height):
    max_area=0
    n=len(height)
    l,r=0,n-1
    while l<r:
        max_area=max(max_area,(min(height[l],height[r])*(r-l)))
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return max_area
    
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
