def m():
    x = int(input())
    a = 100
    ans = 0
    while a < x:
        a = int(a*1.01)
        ans += 1
    return ans


print(m())
