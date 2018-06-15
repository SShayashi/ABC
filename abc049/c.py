def m():
    s = str(input())
    d = ["dream", "dreamer"]
    e = ["erase", "eraser"]
    i = len(s)
    while i >= 5:
        if s[i-5:i] == d[0]:
            i -= 5
            continue
        if s[i-5:i] == e[0]:
            i -= 5
            continue
        if s[i-7:i] == d[1]:
            i -= 7
            continue
        if s[i-6:i] == e[1]:
            i -= 6
            continue
        return "NO"
    return "YES"

print(m())