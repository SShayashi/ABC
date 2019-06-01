import itertools

def m():
    a = map(int, input().split())
    b = itertools.combinations(a, 3)
    ans = []
    for i in b:
        ans.append(sum(i))
    ans.sort(reverse=True)
    return ans[2]

print(m())