class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]    
        else:    
            pascal=[[1],[1,1]]
            i=2
            while len(pascal)!=numRows:
                j=1
                row=[1]
                while len(row)<=i and j<=i:
                    if j==i:
                        row.append(1)
                        j+=1
                        break
                    else:
                        row.append((pascal[i-1][j-1])+(pascal[i-1][j]))
                        j+=1
                pascal.append(row)
                i+=1
            return pascal
        
        # print("Triangle list for numsRows",numRows)
        # if numRows==1:
        #     return [[1]]
        # elif numRows==2:
        #     return [[1],[1,1]]    
        # else:
        #     pascal = [[1],[1,1]]
        #             # 0    1
        #     lastList = []
        #     for i in range(2,numRows):
        #         # print(i,end=" ")
        #         row = pascal[-1]
                
        #         lastList.append(1)

        #         # row ==> [1,1]
        #         for j in range(1,len(row)): # range(2)==>0,1
        #             lastList.append(row[j-1]+row[j])
        #         lastList.append(1)
        #         pascal.append(lastList)
        #         lastList = []
        #     return pascal
            