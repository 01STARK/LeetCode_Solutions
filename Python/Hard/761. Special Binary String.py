def makeLargestSpecial(s):
    n=len(s)
    subarray=[]
    for i in range(n-1):
        #Find SubStrings
        j=i+1
        if s[i:j].count('1')==s[i:j].count('0') and s[i:j].startswith('1'*n/2):
            subarray.append((i,j))

    print(subarray)

s='11011000'

        