def m():
    A, B, X = map(int, input().split())
    if A > X:
        return 'NO'
    if X > A+B:
        return 'NO'
    return 'YES'


print(m())
