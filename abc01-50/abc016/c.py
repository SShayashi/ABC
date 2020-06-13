def m():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A].append(B)
        G[B].append(A)

    def friends(blocks, f):
        cnt = 0
        tomodachi = []
        for a in f:
            for b in G[a]:
                if b in blocks:
                    continue
                tomodachi.append(b)
        return len(set(tomodachi))

    for i in range(1, N + 1):
        print(friends([i]+G[i], G[i]))
    return


m()
