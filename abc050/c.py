MOD = 10 ** 9 + 7

def m():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == 0:
        tmp = 2
        for i in range(1, n, 2):
            for k in range(2):
                if a[i+k] != tmp:
                    return 0
            tmp += 2
        tmp -=2
        return (2 ** (tmp//2))%MOD

    if a[0] == 1:
        tmp = 1
        for i in range(0, n, 2):
            for k in range(2):
                if a[i+k] != tmp:
                    return 0
            tmp += 2
        tmp -= 1
        return (2 ** (tmp//2))%MOD
    return 0


print(m())