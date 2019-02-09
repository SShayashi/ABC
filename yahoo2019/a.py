n, k = map(int, input().split())
ans = 0
for i in range(1, n+1, 2):
    ans += 1
if ans >= k:
    print("YES")
else:
    print("NO")