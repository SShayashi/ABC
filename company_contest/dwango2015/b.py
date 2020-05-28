def m():
    S = str(input())
    S = S.replace('25', 'X')
    for i in range(10):
        S = S.replace(str(i), 'Z')
    A = S.split('Z')
    ans = 0
    for a in A:
        lenght = len(a)
        ans += (lenght * (lenght + 1)) // 2
    return ans


print(m())
