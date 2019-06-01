S = input()
a = ['A', 'C', 'G', 'T']
cnt = 0
ans = 0
for c in S:
    if c in a:
       cnt +=1
       ans = max(ans, cnt)
    else:
       cnt = 0
print(ans)