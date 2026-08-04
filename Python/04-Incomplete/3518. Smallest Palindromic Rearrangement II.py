from collections import defaultdict
import math

class Solution:
    def formula(self, count, remaining_length):
        numerator = math.factorial(remaining_length)
        denominator = 1
        for val in count.values():
            denominator *= math.factorial(val)
        return numerator // denominator

    def smallestPalindrome(self, s, k):
        n = len(s)
        if n < 2:
            return s if k == 1 else ""

        if n % 2 == 0:
            front_len = n // 2
            mid = ''
        else:
            front_len = n // 2
            mid = s[n // 2]

        # Build count of letters available for the FRONT HALF only
        # (each pair contributes 1 to the front half's budget)
        full_count = defaultdict(int)
        for ch in s:
            full_count[ch] += 1

        count = {ch: cnt // 2 for ch, cnt in full_count.items() if cnt // 2 > 0}

        remaining_length = front_len
        result_chars = []

        for _ in range(front_len):
            # try letters in alphabetical order
            for letter in sorted(count.keys()):
                # tentatively place this letter
                count[letter] -= 1
                remaining_length -= 1

                if count[letter] == 0:
                    del count[letter]

                ways = self.formula(count, remaining_length)

                if k <= ways:
                    # confirmed! keep it, move to next position
                    result_chars.append(letter)
                    break
                else:
                    # not enough — undo, subtract, try next letter
                    k -= ways
                    count[letter] = count.get(letter, 0) + 1
                    remaining_length += 1
            else:
                # no letter worked — shouldn't happen if k is valid
                return ""

        front = ''.join(result_chars)
        return front + mid + front[::-1]


so = Solution()
s = "bacab"; k = 1
print(so.smallestPalindrome(s, k))