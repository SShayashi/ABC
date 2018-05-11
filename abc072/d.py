def m():
    def is_satisfied(p):
        for i in range(N):
            if i + 1 == p[i]: return False
        return True

    def swap(i):
        tmp = p[i]
        p[i] = p[i + 1]
        p[i + 1] = tmp

    N = int(input())
    p = list(map(int, input().split()))
    if is_satisfied(p):
        return 0

    cnt = 0
    for i in range(N):
        if i + 1 == p[i]:
            if i + 1 == N:
                cnt += 1
                tmp = p[i - 1]
                p[i - 1] = p[i]
                p[i] = tmp
            else:
                swap(i)
                cnt += 1
    return cnt


print(m())
