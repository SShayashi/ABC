N = int(input())

b = []
a = [int(input()) for i in range(N)]

cnt = 0
for i in a:
    if i in b:
        pass
    else:
        b.append(i)
print(len(b))
