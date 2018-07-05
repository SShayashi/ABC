def m():
    s = str(input())
    ans = 0
    a = s.split("+")
    for i in range(len(a)):
        if "0" in a[i]:
            continue
        else:
            ans += 1
    return ans
print(m())