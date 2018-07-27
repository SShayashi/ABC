NUM = 96
def m():
    n,k = map(int, input().split())
    s = input()
    a = list(set(s))
    a.sort()
    ans = ord(a[0]) - NUM
    k -=1
    for i in range(1, len(a)):
        if k == 0:
            break
        if ord(a[i]) == ord(a[i-1])+1:
            continue
        ans += ord(a[i])-NUM
        k -= 1
    if k != 0:
        return -1

    return ans
print(m())