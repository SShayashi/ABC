def m():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    cnt = 0
    for a in A:
        for b in B:
            for c in C:
                if a < b and b < c:
                    cnt +=1
    return cnt


print(m())