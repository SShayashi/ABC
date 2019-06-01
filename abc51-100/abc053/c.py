def m():
    x = int(input())
    ans = (x // 11) * 2
    if x % 11 == 0:
        return ans
    if x % 11 <= 6:
        return ans + 1
    return ans + 2

print(m())