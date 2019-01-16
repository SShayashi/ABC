N = int(input())
V = list(map(int, input().split()))


def m():
    first = V[0::2]
    second = V[1::2]
    fdic = {}
    sdic = {}
    for i in range(N//2):
        if fdic.get(first[i], 0) == 0:
            fdic[first[i]] = 1
        else:
            fdic[first[i]] +=1

        if sdic.get(second[i], 0) == 0:
            sdic[second[i]] = 1
        else:
            sdic[second[i]] +=1
    flist = list(fdic.items())
    slist = list(sdic.items())

    flist.sort(reverse=True, key=lambda x:x[1])
    slist.sort(reverse=True, key=lambda x:x[1])

    if flist[0][0] != slist[0][0] and len(flist) == 1 and len(slist) == 1:
        return 0


    if flist[0][0] != slist[0][0]:
        ans = 0
        for k, v in flist[1:]:
            ans += v
        for k, v in slist[1:]:
            ans += v
        return ans

    if flist[0][1] == slist[0][1]:
        return N//2

    if flist[0][1] > slist[0][1]:
        ans = 0
        for k, v in flist[1:]:
            ans += v
        for k, v in slist[2:]:
            ans += v
        ans += slist[0][0]
        return ans
    else:
        ans = 0
        for k, v in slist[1:]:
            ans += v
        for k, v in flist[2:]:
            ans += v
        ans += flist[0][0]
        return ans

print(m())