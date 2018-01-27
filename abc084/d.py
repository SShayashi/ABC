def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q & 1 == 0: return False
    return pow(2, q - 1, q) == 1


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

            if is_prime(x) and is_prime((x+1)//2):
                dp[x] = 1
                cnt += 1
            else:
                dp[x] = 0

        print(cnt)

main()
