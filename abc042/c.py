def m():
    def is_included(i,d):
        s = str(i)
        for j in d:
            if str(j) in s:
                return True
        return False
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    for i in range(n, n*10):
        if not is_included(i,d):
            return i
    return 0
print(m())