def main():
    N = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    for i in range(1, N):
        a1[i] += a1[i - 1]
        a2[i] += a2[i - 1]

    max_ame = 0
    for i in range(0, N):
        if i == 0:
            ame = a1[0]
            ame += a2[N-1]
            max_ame = ame
            continue

        ame = a1[i] + (a2[N-1] - a2[i - 1])
        max_ame = max(max_ame, ame)

    return print(max_ame)


main()
