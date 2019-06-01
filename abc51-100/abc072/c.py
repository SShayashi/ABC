MAX = 100000
def m():
    N = int(input())
    a = list(map(int, input().split()))
    t = [0] * (MAX + 1)

    for i in range(N): t[a[i]] += 1
    ans = 0
    tmp = 0
    for n in range(1, MAX):
        ans = max(t[n - 1] + t[n] + t[n + 1], ans)
    return ans

print(m())
