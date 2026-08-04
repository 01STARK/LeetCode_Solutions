class Solution:
    def search(self, nums, target):
        s,e=0,len(nums)-1

        while s<e:
            mid = (s+e)//2

            if nums[mid]==target:
                return mid

            # sorted part
            if nums[s]<=nums[mid]:
                # inside range 
                if nums[s]<=target<=nums[mid]:
                    e=mid-1
                # not in range
                else:
                    s = mid+1
            else:
                if nums[mid]<=target<=nums[e]:
                    s=mid+1
                else:
                    e=mid-1
        if nums[e]==target:
            return e
        return -1