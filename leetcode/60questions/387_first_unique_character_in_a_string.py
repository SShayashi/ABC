class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        length = len(s)
        for i in range(length):
            if d.get(s[i], '') == '':
                d[s[i]] = i
            else:
                d[s[i]] = float('inf')
        ans = float('inf')
        for j in d.values():
            ans = min(ans, j)
        if ans == float('inf'):
            return -1
        else:
            return ans
