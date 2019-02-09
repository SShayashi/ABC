def m():
    K, A, B = map(int, input().split())
    ans = 0
    if B - A <= 2:
        return K+1
    if K <= A:
        return K+1
    cnt = K-A+1

    amari = 0
    if cnt % 2 == 1:
        amari = 1
    ans += (cnt//2) * B - ((cnt//2)-1)*A
    ans += amari
    return ans

print(m())