def m():
    n = int(input())
    s = str(input())
    ans = 0
    for i in range(1, n):
        cnt = 0
        left = set(s[i:])
        right = set(s[:i])
        for j in left:
            if j in right:
                cnt +=1
        ans = max(cnt, ans)
    return ans

print(m())