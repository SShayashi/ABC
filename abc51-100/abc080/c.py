def ans():
    tmp = -9999999999999
    N = int(input())
    F = [list(map(int, input().split())) for i in range(N)]
    P = [list(map(int, input().split())) for i in range(N)]

    def calculate(B):
        v = []
        for n in range(N):
            mcnt = 0
            for k in range(10):
                if B[k] == '1' and F[n][k] == 1:
                    mcnt += 1
            v.append(P[n][mcnt])
        return sum(v)

    for i in range(1, 1 << 10):
        bi = bin(i)
        bi = bi[2:]
        bi = '0' * (10 - len(bi)) + bi
        tmp = max(tmp, calculate(bi))
    return print(tmp)


ans()



# def main():
#     N = int(input())
#     F = [list(map(int, input().split())) for i in range(N)]
#     P = [list(map(int, input().split())) for i in range(N)]
#     mp = 0
#     fc = [sum(f) for f in F]
#     r = []
#     diff = [p[0] - p[1] for p in P]
#     flag = 0
#     for i, p in enumerate(P):
#         m = max(p[:fc[i] + 1])
#         if p[0] <= m:
#             flag = 1
#         r.append(m)
#
#     if flag == 0:
#         mini = min(diff)
#         ind = diff.index(mini)
#         r[ind] = p[1]
#
#     return print(sum(r))
