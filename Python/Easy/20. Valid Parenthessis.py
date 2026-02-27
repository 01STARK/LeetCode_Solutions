class Solution:
    def isValid(self, s: str) -> bool:
        pile = []
        brack={
            ')':'(',
            ']':'[',
            '}':'{'
            }

        for i in s:
            if i in brack:
                top = pile.pop() if pile else '#'
                if brack[i] != top:
                    return False
            else:
                pile.append(i)
        return len(pile)==0