from typing import List

from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = {}
        count_dict = {i:0 for i in ascii_lowercase }
        for s in strs:
            d = count_dict.copy()
            for c in s:
                d[c] += 1
            key = ""
            for c in ascii_lowercase:
                if d[c] == 0:
                    continue
                key += c*d[c]
            if key in answers.keys():
                answers[key].append(s)
            else:
                answers[key] = [s]
        return list(answers.values())


x = Solution()
print(x.groupAnagrams(
    ["mod", "mop", "pip", "tug", "hop", "dog", "met", "zoe", "axe", "mug", "fdr", "for", "fro", "fdr", "pap", "ray",
     "lop", "nth", "old", "eva", "ell", "mci", "wee", "ind", "but", "all", "her", "lew", "ken", "awl", "law", "rim",
     "zit", "did", "yam", "not", "ref", "lao", "gab", "sax", "cup", "new", "job", "new", "del", "gap", "win", "pot",
     "lam", "mgm", "yup", "hon", "khz", "sop", "has", "era", "ark"]))
