def m():
    k = int(input())
    if k % 2 == 0:
        return (k//2) **2
    else:
        return (k//2)*((k//2)+1)

print(m())