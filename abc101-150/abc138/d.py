import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def m():
    n, q = map(int, input().split())
    tree = [[] for _ in range(n + 1)]
    for i in range(1, n):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    counter = [0] * (n + 1)
    for _ in range(q):
        p, x = map(int, input().split())
        counter[p] += x

    ans = [0] * (n + 1)
    visited = []
    add_visited = visited.append
    def dfs(root, point):
        point += counter[root]
        ans[root] = point
        add_visited(root)
        for j in tree[root]:
            if j in visited:
                continue
            dfs(j, point)
        return

    dfs(1, 0)
    for i in range(1, n + 1):
        print(ans[i], '', end='')
    return ans


m()
