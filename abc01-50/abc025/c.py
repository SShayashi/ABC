def m():
    b1 = list(map(int, input().split()))
    b2 = list(map(int, input().split()))
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))
    score = sum(b1) + sum(b2) + sum(c1) + sum(c2) + sum(c3)
    for i in range(3):
        for j in range(3):
            pass


print(m())