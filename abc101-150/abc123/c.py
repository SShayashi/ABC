n = int(input())
a = []
for _ in range(5):
    a.append(int(input()))


def m():
    if n == 1:
        return 5
    if min(a) == 1:
        return n+4
    return n // min(a) + 5


print(m())
