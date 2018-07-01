def m():
    n = int(input())
    a = list(map(int, input().split()))
    new_a = []
    for i in range(1, n+1):
        new_a.append((i,a[i-1]))
    new_a.sort(reverse=True,key=lambda x:x[1])
    for j in new_a:
        print(j[0])

m()