def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a,b):
    return a * b // gcd(a,b)

def m():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = T[0]
    for i in range(1,N):
        ans = lcm(ans,T[i])
    return ans

print(m())