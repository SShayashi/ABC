class Solution:
    def myAtoi(self, string: str) -> int:
        INF_MAX = 2 ** 31 - 1
        INF_MIN = -2 ** 31
        empty = ' '
        mark = 1
        left = 0
        right = len(string)
        if len(string) == string.count(" "):
            return 0
        for i in range(len(string)):
            if string[i] == empty:
                continue
            else:
                left = i
                break
        for i in range(left + 1, len(string)):
            if string[i] == empty:
                right = i
                break
            else:
                continue

        if string[left] == '+':
            left += 1
        elif string[left] == '-':
            left += 1
            mark *= -1
        else:
            pass
        target = string[left:right]
        if len(target) == 0:
            return 0
        dots = 0
        for c in target:
            if c.isnumeric():
                continue
            elif c == '.':
                dots += 1
            else:
                return 0
        if dots > 1:
            return 0
        ans = int(eval(target)) * mark
        if INF_MIN <= ans <= INF_MAX:
            return ans
        elif ans >= INF_MAX:
            return INF_MAX
        else:
            return INF_MIN


x = Solution()
print(x.myAtoi("+")) #

print(x.myAtoi("3.1413")) # expect 3
print(x.myAtoi("42"))
print(x.myAtoi("4193 with words"))
print(x.myAtoi("-91283472332"))