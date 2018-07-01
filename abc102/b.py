def m():
    n = int(input())
    a = list(map(int, input().split()))
    return abs(max(a)-min(a))

print(m())