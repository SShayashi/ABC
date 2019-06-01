def m():
    s, c = map(int, input().split())
    if s >= c:
        return c//2
    ans = s
    ans += (c - s*2) // 4
    return ans

print(m())