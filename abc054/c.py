def m():
    n, m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    ans = 0
    import itertools
    perm = list(itertools.permutations([j for j in range(1,n+1)]))
    for l in perm:
        if l[0] != 1:
            continue
        flag = 0
        for i in range(1, len(l)):
            if l[i] in g[l[i-1]]:
                pass
            else:
                flag = 1
                break
        if flag:
            continue
        ans+=1
    return ans

print(m())