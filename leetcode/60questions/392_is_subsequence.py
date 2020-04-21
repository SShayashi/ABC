class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if len(s) == 0:
            return True
        spos = 0
        length = len(s)
        for ct in t:
            if ct == s[spos]:
                spos += 1
            if spos >= length:
                return True
        return False



