import queue
import sys
def input(): return sys.stdin.readline().rstrip()

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

    que = queue.Queue()
    visited = [False] * (n+1)

    def bfs(root, base):
        base += counter[root]
        visited[root] = True
        for e in tree[root]:
            if visited[e]:
                continue
            que.put(e)
            counter[e] += base

        while not que.empty():
            x = que.get()
            point = counter[x]
            visited[x] = True
            for e in tree[x]:
                if visited[e]:
                    continue
                que.put(e)
                counter[e] += point

    bfs(1, 0)
    print(*counter[1:])
    return


m()
