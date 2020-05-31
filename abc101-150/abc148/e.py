def m():
    n = int(input())
    if n % 2 != 0: return 0
    i = 1
    ans = 0
    while True:
        tmp = n // (2*5**i) 
        if tmp == 0:
            break
        ans += tmp
        i+=1
    return ans

print(m())