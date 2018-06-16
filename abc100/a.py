def m():
    a, b = map(int, input().split())
    if a <=8 and b <= 8:
        return "Yay!"
    return ":("

print(m())