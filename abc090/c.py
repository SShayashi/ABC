def m():
    n, m = map(int, input().split())
    if n == 1 and m == 1:
        return 1
    if n == 1:
        return m-2
    if m == 1:
        return n-2
    if n == 2 or m == 2:
        return 0
    return (m-2) * (n-2)

print(m())