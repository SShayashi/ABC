import itertools
import queue

MAX = 999999999
def m():
    N, M, R = map(int, input().split())
    r = list(map(int, input().split()))
    graph = [[MAX for _ in range(N+1)] for _ in range(N+1)]
    for i in range(M):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c

    def solve(d):
        for k in range(1,N+1):
            for j in range(1,N+1):
                for n in range(1,N+1):
                    d[j][n] = min(d[j][n], d[j][k] + d[k][n])
        return d

    e = solve(graph)
    ans = MAX
    for l in itertools.permutations(r):
        cost = 0
        for i in range(1,R):
            cost += e[l[i-1]][l[i]]
        ans = min(cost, ans)
    return ans

def someone_ans():
    N, M, R = map(int, input().split())
    r = list(map(int, input().split()))
    graph = [[MAX for _ in range(N+1)] for _ in range(N+1)]
    for i in range(M):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c

    def dijkstra(d, index):
        q = queue.PriorityQueue()
        checked = []
        q.put((0, index))
        while not q.empty():
            # qの中の最小値だす
            cost, i = q.get()
            if i in checked: continue
            if cost == MAX: continue
            checked.append(i)
            d[index][i] = cost
            for j,v in enumerate(graph[i]):
                if v == MAX: continue
                if (j in checked) == False:
                    q.put((cost + graph[i][j], j))

        return d[index]
    ds = [[MAX for _ in range(N+1)] for _ in range(N+1)]

    # 自分から自分までの距離は0
    for i in range(1,N+1):
        ds[i][i] = 0

    for i in range(1,N+1):
        # 各地点からその他の地点までの最短距離を求める
        ds[i] = dijkstra(ds, i)
        for k in range(1,N+1):
            # k->iまでの距離はi->kと一緒
            ds[k][i] = ds[i][k]

    ans = MAX
    for l in itertools.permutations(r):
        cost = 0
        for i in range(1,R):
            cost += ds[l[i-1]][l[i]]
        ans = min(cost, ans)
    return ans

print(someone_ans())
# print(m())