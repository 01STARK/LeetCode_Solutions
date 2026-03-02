class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(opn,clse,s):
            if len(s)==2*n:
                res.append(s)
                return res
            if opn<n:
                dfs(opn+1,clse,s+'(')
            if clse<opn:
                dfs(opn,clse+1,s+')')
        dfs(0,0,'')
        return res