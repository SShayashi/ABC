def m():
    s = input()
    k = int(input())
    a = set()
    for i in range(len(s)):
        for j in range(5):
            a.add(s[i:i+j+1])
    b = list(a)
    b.sort()
    return b[k-1]

print(m())