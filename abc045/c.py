def m():
    s = str(input())
    ans = 0
    # iを+の数とする
    for i in range(len(s)):
        if i == 0:
            ans += int(s)
            continue

        while i >=0:
            tmp = s[0:1]

            pass
        pass
    pass

def ans():
    s = list(input())
    sl = len(s)
    ans = 0
    for i in range(1 << sl-1):
        tmp = s[0]
        for j in range(sl-1):
            if i&(1<<j):
                tmp += "+"
            tmp +=s[j+1]
        ans +=eval(tmp)
print(ans())