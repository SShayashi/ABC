def m():
    s = str(input())
    k = int(input())
    if len(s) >= k:
        for i in s[:k]:
            if i != "1":
                return i
        return 1
    else:
        for i in s:
            if i != "1":
                return i


print(m())