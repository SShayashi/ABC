n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
def main():
    d = {}
    for i in range(n, 0, -1): d[i] = n-i
    for i in range(1, m+1): d[a[i-1]] = n+i
    l = list(d.items())
    l.sort(reverse=True, key=lambda x:x[1])
    for j in l:
        print(j[0])
    pass
main()