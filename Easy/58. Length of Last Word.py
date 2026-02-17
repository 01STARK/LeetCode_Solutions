# def lengthOfLastWord(s):
#         r=s[::-1].strip()
#         n=len(r)
#         start=0
#         stop=0
#         for i in range(n):
#             if start==0 and s[i]!=' ':
#                 start=int(i-1)
#                 print('start ',start)
#             if stop==0 and start!=0 and s[i]==' ':
#                 stop=int(i)
#                 print('stop ',stop)
#         return len(r[start:stop])
# s = "   fly me   to   the moon  "
# print(lengthOfLastWord(s))

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        length = 0
        # Count last word characters
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length