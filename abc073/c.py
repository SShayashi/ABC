def m():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = []
    for a in A: ans.remove(a) if a in ans else ans.append(a)
    return len(ans)

print(m())
