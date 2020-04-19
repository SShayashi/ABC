def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(1, n+1):
        d[i] = 0
    for b in a:
        d[b] +=1
    for k,v in d.items():
        print(v)
main()