def main():
    s = list(input())
    s.reverse()
    MOD = 2019
    tot = 0
    ans = 0
    d = [0 for _ in range(MOD)]
    for i in range(len(s)):
        d[tot] += 1
        x = pow(10, i, MOD)
        p = int(s[i]) * x
        p %= MOD
        tot = (tot + p) % MOD
        ans += d[tot]
    return ans


if __name__ == '__main__':
    print(main())
