def main():
    N, M = map(int, input().split())
    field = [0 for _ in range(1000000)]
    info = []
    for i in range(M):
        L, R, D = map(int, input().split())
        info.append([L, R, D])

    for i in info:
        L, R, D = i
        if field[L] != 0 and field[L] != L:
            return print('No')
        if field[L + D] != 0 and field[L + D] != R:
            return print('No')
        field[L] = L
        field[L + D] = R

    return print('Yes')


main()
