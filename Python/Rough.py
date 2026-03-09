import itertools
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        res=[]
        interval=limit+1
        n=zero+one
        final=[]
        temp_list = [list(combo) for combo in itertools.product([0, 1], repeat=n)]
        for i in temp_list:
            for j  in range(n-interval):
                if i.count(1)==one and i[j:j+interval].count(1)<interval:
                    res.append(i)
        # for i in res:
        #     for j in range(len(i)-interval):
        #         if i[j:j+interval].count(0)<interval:
        #             final.append(i)
        res=[*set(res)]
        print(len(res))
        
        
        
so=Solution()
print(so.numberOfStableArrays(3,3,2))