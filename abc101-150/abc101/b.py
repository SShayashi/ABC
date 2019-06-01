def m():
    n = str(input())
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    if int(n) % s == 0:
        return "Yes"
    else:
        return "No"

print(m())