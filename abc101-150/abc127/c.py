N, M = map(int, input().split())
lmax, rmin = 0, N
for _ in range(M):
    l, r = map(int, input().split())
    lmax = max(lmax, l)
    rmin = min(rmin, r)

if lmax == rmin:
    print(1)
elif lmax > rmin:
    print(0)
else:
    print(rmin-lmax+1)
