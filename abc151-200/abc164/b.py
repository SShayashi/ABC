a, b, c, d = map(int, input().split())
x = -(-a // d)
y = -(-c // b)
if x == y:
    print('Yes')
if x < y:
    print('No')
if x > y:
    print('Yes')