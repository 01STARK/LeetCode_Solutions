class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # count_substring = 0
        # for p in patterns:
        #     if word.find(p)!= -1:
        #         count_substring+=1

        # return count_substring
        count=0
        for i in patterns:
            if i in word:
                count+=1        
        return count
