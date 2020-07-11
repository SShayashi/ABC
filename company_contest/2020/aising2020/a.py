L, R, d = map(int, input().split())
ans = (R // d) - ((L-1)//d)
print(ans)