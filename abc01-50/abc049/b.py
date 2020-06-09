a, b, x = map(int, input().split())
s = 1 if a % x == 0 else 0
print(b // x - a // x + s )
