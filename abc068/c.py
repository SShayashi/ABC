def main():
    n, m = map(int, input().split())
    a, b = [], []
    from_1 = set()
    to_n = set()
    for _ in range(m):
        x, y = map(int, input().split())
        if x == 1:
            from_1.add(y)
            continue
        if y == n:
            to_n.add(x)
            continue
    ans = from_1 & to_n
    if ans:
        return "POSSIBLE"

    return 'IMPOSSIBLE'


print(main())