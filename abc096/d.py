MAX = 55555
def get_prime_array(N):
    f = [True] * (N + 1)
    for i in range(2, N + 1):
        if f[i]:
            for j in range(i + i, N + 1, i):
                f[j] = False
    return f

def m():
    n = int(input())
    f = get_prime_array(MAX)
    a = []
    for i in range(6, len(f)):
        if f[i] and i % 5 == 1:
            a.append(i)
            if len(a) == n:
                break
    ans = ""
    for j in a:
        ans += str(j) + " "
    return ans

print(m())