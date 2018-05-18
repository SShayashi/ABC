def m():
    N = int(input())
    a = list(map(int, input().split()))
    fours = []
    twes = []
    others = []
    for i in range(N):
        if a[i] % 4 == 0:
            fours.append(a[i])
            continue

        if a[i] % 2 == 0:
            twes.append(a[i])
            continue
        others.append(a[i])

    len4s = len(fours)
    len2s = len(twes)
    others = len(others)
    if (others + len2s) <= len4s + 1:
        return 'Yes'
    if others <= len4s + 1:
        if len2s % 2 == 0:
            return 'Yes'
    if len4s == 0 and others ==0:
        if len2s % 2 == 0:
            return 'Yes'
    return 'No'


print(m())
