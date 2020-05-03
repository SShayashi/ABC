def m():
    n, k = map(int, input().split())
    dic = {}
    for _ in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for i in a:
            dic[i] = 1
    return n - len(dic.keys())


print(m())
