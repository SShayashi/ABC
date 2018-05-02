def solve_area(v):
    area = 0
    for i in range(1, len(v)):
        area += (v[i] + v[i-1]) * 0.25
    return area

def m():
    N = int(input())
    t = [int(i) for i in input().split()]
    v = [int(j) for j in input().split()]
    maxtime = sum(t)
    max_v = [0] * (maxtime*2+1)
    endpoint = 0
    for n in range(N):
        for k in range(endpoint, endpoint + t[n]*2):
            max_v[k] = v[n]
        endpoint = k +1

    max_v[0] = 0
    for m in range(1, maxtime*2+1):
        max_v[m] = min(max_v[m-1]+0.5, max_v[m])

    max_v[maxtime*2] = 0
    for p in range(maxtime*2 - 1, 0, -1):
        max_v[p] = min(max_v[p+1]+0.5, max_v[p])

    ans = solve_area(max_v)
    return ans

print(m())