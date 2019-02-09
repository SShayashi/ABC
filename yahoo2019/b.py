
def m():
    d = {1: 0, 2: 0, 3: 0, 4: 0}
    for _ in range(3):
        a, b = map(int, input().split())
        d[a] +=1
        d[b] +=1

    cnt1 = 0
    cnt2 = 0
    for k,v in d.items():
        if v == 1:
            cnt1 += 1
            continue

        if v == 2:
            cnt2 += 1
            continue
        return "NO"
    if cnt1 == 2 and cnt2 == 2:
        return "YES"
    else:
        return "NO"
print(m())
