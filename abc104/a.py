def m():
    r = int(input())
    if r < 1200:
        return "ABC"
    if r < 2800:
        return "ARC"
    return "AGC"

print(m())