import queue
MAX = 10 ** 10
def m():
    def dijkstra(ds, start):
        q = queue.PriorityQueue()
        visited = []
        for to, cost in graph[start]:
            q.put((cost, to))
        visited.append(start)
        while not q.empty():
            cost, to = q.get()
            if to in visited: continue
            if cost == MAX: continue
            visited.append(to)
            ds[start][to] = cost
            for k, cost in graph[to]:
                if (k in visited) == False:
                    q.put((cost + ds[start][to], k))
        return ds

    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(1,n):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    q, k = map(int, input().split())
    ds = [[MAX for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1): ds[i][i] = 0
    ds = dijkstra(ds, k)
    for _ in range(q):
        x, y = map(int, input().split())
        ds = dijkstra(ds, x)
        print(ds[x][k] + ds[k][y])

m()