def m():
    N = int(input())
    A, B = map(int, input().split())
    P = list(map(int, input().split()))
    tmp = [0] * 3
    for i in P:
        if i <= A:
            tmp[0] += 1
        elif i > A and i <= B:
            tmp[1] += 1
        elif i > B:
            tmp[2] += 1
    return min(tmp)

print(m())