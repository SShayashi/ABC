import itertools
def m():
    n, cn = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(cn)]
    c = [list(map(int, input().split())) for _ in range(n)]
    l = [[] for _ in range(3)]
    ans = [[] for _ in range(3)]
    for i in range(n):
        for j in range(n):
            l[(i+1+j+1) % 3].append(c[i][j])

    for k in range(3):
        for s in range(cn):
            cost = 0
            for p in l[k]:
                cost += d[p-1][s]
            ans[k].append((s,cost))

    for k in range(3):
        ans[k].sort(key=lambda x: x[1])

    result = 999999999
    for elem in itertools.permutations(range(3)):
        used = []
        tmp = 0
        for e in elem:
            i = 0
            while len(used) < 3:
                if ans[e][i][0] in used:
                    i += 1
                    continue
                tmp += ans[e][i][1]
                used.append(ans[e][i][0])
                break
        result = min(result, tmp)
    return result

print(m())