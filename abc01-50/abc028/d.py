N, K = map(int, input().split())
a = (N - K) * (K - 1) * 6
b = (N - 1) * 3
c = 1
d = a + b + c
e = pow(N, 3)
print(d / e)
