class Solution:
    
    def binaryGap(self, n: int) -> int:
        binary=bin(n)[2:]
        #print("Inary arr: ",binary)
        index=[]
        condition=False
        for i in range(len(binary)):
            if binary[i]=='1':
                index.append(i)
        #print('index arr: ',index)

        max_gap = 0
        for i in range(len(index)-1):
            max_gap = max(max_gap,abs(index[i]-index[i+1]))
        
        return (max_gap)
    
