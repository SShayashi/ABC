import queue


def m():
    N, M = map(int, input().split())
    q = queue.PriorityQueue()
    A = list(map(int, input().split()))
    ans = []
    for a in A:
        q.put(-a)
    while M > 0:
        x = -q.get()
        x = -(x >> 1)
        M -= 1
        q.put(x)
    while not q.empty(): ans.append(q.get())
    return abs(sum(ans))


print(m())
