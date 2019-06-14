N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()
def m():
    ans = 0
    time = 0
    while time < N:
        high = T[time] + K
        for i in range(C):
            if time >= N:
                break
            if T[time] <= high:
                time += 1
            else:
                break
        ans += 1
    return ans
print(m())