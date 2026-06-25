class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # txt = {'b':0,'a':0,'l':0,'o':0,'n':0}
        # n=len(text)
        # for i in range(n):
        #     if text[i] in {'b','a','l','o','n'}:
        #         txt[text[i]]+=1

        # txt['l']=txt['l']//2 ; txt['o']=txt['o']//2        
        # return min(txt.values())
        freq = Counter(text)
        
        return min(freq['b'],freq['a'],freq['l'] // 2,freq['o'] // 2,freq['n'])