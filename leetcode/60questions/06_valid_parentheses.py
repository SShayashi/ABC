class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        begins = ['(', '{', '[']
        ends = [')', '}', ']']
        for i in range(len(s)):
            if s[i] in begins:
                stack.append(s[i])
                continue
            if len(stack) == 0:
                return False

            begin = stack.pop()
            if ends.index(s[i]) != begins.index(begin):
                return False
        if len(stack) != 0:
            return False
        return True

s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))