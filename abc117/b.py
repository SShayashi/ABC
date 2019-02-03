N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
m = L[0]
s = sum(L[1:])
if m < s:
    print('Yes')
else:
    print('No')
