def main():
    n = int(input())
    # 2で何回割れるか
    i = 0
    m = n
    while m > 1:
        m //= 2
        i += 1
    # 2で奇数回割れるなら tはx2，aはx2+1
    if i %2 == 1:
        r = [0,1]
    else:
        r = [1,0]
    a,j = 1,0
    while a <= n:
        a = a*2 + r[j]
        j ^=1
    ans = ["Takahashi", "Aoki"]
    return ans[j]

print(main())