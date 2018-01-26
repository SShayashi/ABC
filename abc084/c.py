
def main():
    N = int(input())

    x = [[int(a) for a in input().split()] for i in range(N - 1)]

    for i in range(N):
        time = 0
        for a in range(i, N-1):
            C = x[a][0]
            S = x[a][1]
            F = x[a][2]
            time = max(time, S)
            if time % F == 0:
                pass
            else:
                time = time + F - time % F
            time += C
        print(time)

main()