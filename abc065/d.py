def main():

    def prime():
        visited = []

        pass

    n = int(input())
    X, Y = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        X.append((x,y))
        Y.append((x,y))
    X.sort(key=lambda x:x[0])
    Y.sort(key=lambda x:x[1])
    l = list(zip(X,Y))


def someone_ans():
    n = int(input())
    towns = []
    for i in range(n):
        x, y = map(int, input().split())
        towns.append((i,x,y)) # 要素の中に番号いれておくべきだった


    adj = [[] for _ in range(n)]
    for xy in [1,2]:
        towns.sort(key=lambda t: t[xy])
        for i in range(n - 1):
            t1 = towns[i][0] #街の識別番号とってる
            t2 = towns[i +1][0]
            cost = towns[i + i][xy] - towns[i][xy]
            #　隣接リストを作っている
            adj[t1].append((t2, cost))
            adj[t2].append((t1, cost))

    #ここからプリム法
    import heapq
    pq = []
    heapq.heappush(pq, (0,0))
    done = set()
    ans = 0
    while pq:
        cost, v_now = heapq.heappop(pq)
        if v_now in done:
            continue

        ans += cost
        done.add(v_now)
        if len(done) == n:
            break

        for v, c in adj[v_now]:
            if v not in done:
                heapq.heappush(pq, (c, v))


print(main())