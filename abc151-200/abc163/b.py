def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n - sum(a) < 0:
        return -1
    return n - sum(a)


print(main())
