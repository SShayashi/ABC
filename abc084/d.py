def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q & 1 == 0: return False
    return pow(2, q - 1, q) == 1


def get_prime_array(N):
    f = [0] * (N + 1)
    for i in range(2, N + 1):
        if not f[i]:
            for j in range(i + i, N + 1, i):
                f[j] = 1
    return f


def ans():
    Q = int(input())
    f = get_prime_array(1000001)
    c = [0] * 1000002
    for i in range(3, 1000001, 2):
        if not f[i] and not f[(i + 1) // 2]:
            c[i] += 1

    for i in range(3, 1000000):
        c[i] = c[i] + c[i - 1]

    for _ in range(Q):
        l, r = map(int, input().split())
        print(c[r] - c[l-1])

def main():
    Q = int(input())
    dp = [-1 for _ in range(1000000)]
    for _ in range(Q):
        cnt = 0
        l, r = map(int, input().split())
        for x in range(l, r + 1):
            if dp[x] != -1:
                if dp[x] == 1:
                    cnt += 1
                    continue

            if is_prime(x) and is_prime((x + 1) // 2):
                dp[x] = 1
                cnt += 1
            else:
                dp[x] = 0

        print(cnt)

ans()
# main()
