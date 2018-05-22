def main():
    n = int(input())
    a = list(map(int, input().split()))

    even = a[1::2]
    odd = a[::2]
    ans = []
    if n % 2 == 0:
        even.reverse()
        ans = even + odd
    else:
        odd.reverse()
        ans = odd + even

    to_str = map(str, ans)
    return " ".join(to_str)

print(main())