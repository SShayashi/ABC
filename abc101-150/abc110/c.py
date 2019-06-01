def m():
    s = input()
    t = input()
    a = {chr(i): "" for i in range(97, 97 + 26)}
    b = {chr(i): "" for i in range(97, 97 + 26)}
    n = len(s)
    for i in range(n):
        if a[s[i]] == "":
            a[s[i]] = t[i]
        else:
            if a[s[i]] != t[i]:
                return 'No'
        if b[t[i]] == "":
            b[t[i]] = s[i]
        else:
            if b[t[i]] != s[i]:
                return 'No'
    return 'Yes'
print(m())
