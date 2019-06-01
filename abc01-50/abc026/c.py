import sys
sys.setrecursionlimit(10000000)

def m():
    n = int(input())
    a = [[] for _ in range(n+1)]
    for i in range(1, n):
        b = int(input())
        a[b].append(i+1)
        # a[i+1].append(b)

    def dfs(v,g):
        if len(g[v]) == 0:
            return 1
        tmp_max = 0
        tmp_min = 99999999
        for i in a[v]:
            tmp = dfs(i,g)
            tmp_max = max(tmp_max,tmp)
            tmp_min = min(tmp_min,tmp)
        return tmp_max + tmp_min + 1

    return dfs(1,a)


print(m())