N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]


def m():

    def is_match(x, y):
        for i in range(M):
            for j in range(M):
                if A[x+i][y+j] == B[i][j]:
                    pass
                else:
                    return False
        return True

    for x in range(N-M+1):
        for y in range(N-M+1):
            if is_match(x, y):
                return 'Yes'
            else:
                continue
    return 'No'


print(m())
