

class Solution:
  def findTheDifference(self, s: str = 'abcd', t: str = "abcda") -> str:
        if len(s) == 0:
            return t[0]
        for i in range(len(s)):
            t=t.replace(s[i], '', 1)
        return t[0]
if __name__ == '__main__':
    ob = Solution()
    diff = ob.findTheDifference()
