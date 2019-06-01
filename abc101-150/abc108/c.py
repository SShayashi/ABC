def m():
    n, k = map(int, input().split())
    half = k // 2
    odd = 0
    even = 0
    even_half = 0
    for i in range(1, n+1):
        if k % 2 == 0:
            if i % k == 0:
                even += 1
            if i % k == half:
                even_half += 1
        else:
            if i % k == 0:
                odd += 1
    ans = max(odd ** 3, even ** 3 + even_half ** 3)
    return ans
print(m())