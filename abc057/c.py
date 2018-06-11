def m():
    n = int(input())
    i=1
    div = []
    while i*i <= n:
        if n % i == 0:
            div.append(i)
        i+=1
    a = max(div)
    b = n // a
    d = max(a,b)
    return len(str(d))

print(m())