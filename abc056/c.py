def m():
    x = int(input())
    i = 0
    while (i*(i+1)//2) <= x*2:
        if x <= (i*(i+1)//2):
            return i
        i+=1

print(m())