import queue


def m():
    h, w = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))
    q = queue.Queue()
    for i in range(1, n+1):
        for _ in range(a[i-1]):
            q.put(i)
    # a.sort(reverse=True)
    ans = [[0 for _ in range(w+1)] for _ in range(h+1)]

    for i in range(1, h+1):
        if i % 2 == 1:
            for k in range(1, w+1):
                ans[i][k] = q.get()
        else:
            for k in range(w, 0, -1):
                ans[i][k] = q.get()

    for i in range(1, h+1):
        for k in range(1, w+1):
            print(ans[i][k], end=' ')
        print('')

m()