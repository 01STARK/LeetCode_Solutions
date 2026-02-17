class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        n=len(digits)
        dial=[]
        for digit in digits:
            dial.append(numpad[digit])
        temp_sol=[''.join(pair) for pair in itertools.product(*dial)]
        return temp_sol