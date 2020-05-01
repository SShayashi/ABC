from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = {}
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            p = 0
            for i in range(len(local)):
                if local[i] == '+':
                    break
                p = i
            ans = local[:p + 1]
            d[f'{ans}@{domain}'] = 1
        return len(d.keys())


i = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
out = Solution().numUniqueEmails(i)
print(out)
[].index()