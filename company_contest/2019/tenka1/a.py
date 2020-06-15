a,b,c = map(int, input().split())

if a < b:
    if a <= c and b >= c:
        print('Yes')
    else:
        print('No')
else:
    if b <= c and a >= c:
        print('Yes')
    else:
        print('No')