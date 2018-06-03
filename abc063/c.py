def m():
    n = int(input())
    s = [int(input()) for _ in range(n)]
    tens = 0
    others = []
    for i in range(n):
        if s[i] % 10 == 0:
            tens += s[i]
        else:
            others.append(s[i])
    if len(others) == 0:
        return 0
    total = tens + sum(others)
    if total % 10 == 0:
        return total - min(others)
    else:
        return total
print(m())