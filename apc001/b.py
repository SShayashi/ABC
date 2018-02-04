def main():
    def is_even(n):
        return n % 2 == 0

    def is_odd(n):
        return not is_even(n)

    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if a == b:
        return print('Yes')

    d = [b[i]-a[i] for i in range(N)]
    dif_cnt = 0
    for i in range(N):
        if is_even(a[i]) and is_even(b[i]):
            continue
        if is_odd(a[i]) and is_odd(b[i]):
            continue
        dif_cnt += 1

    sum_d = sum(d)
    if sum_d <= 0:
        return print('No')
    if sum_d % 3 == 0:
        if dif_cnt % 2 == 1 and sum_d > dif_cnt and dif_cnt % 2 == 1:
            return print('Yes')
        elif dif_cnt % 2 == 0 and sum_d > dif_cnt and dif_cnt % 2 == 0:
            return print('Yes')
    return print('No')


main()
