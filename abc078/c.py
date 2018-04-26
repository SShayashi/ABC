def m():
    N, M = map(int, input().split())
    ONE = (N-M)
    count = 2 << (M-1)
    return ((ONE*100)+(M*1900))*count


print(m())