def main():
    def new_A(a1):
        A[1] = a1
        A[2] = C[2][1] - C[1][1] - a1
        A[3] = C[3][1] - C[2][1] - A[2]
        return A

    def check(A):
        B[1] = C[1][1] - A[1]
        B[2] = C[1][2] - A[1]
        B[3] = C[1][3] - A[1]

        for a in range(1,4):
            for b in range(1, 4):
                if C[a][b] != (A[a] +B[b]):
                    return False
        return True

    C = []
    C.append([])
    C.append(list(map(int, ('0 ' + input()).split())))
    C.append(list(map(int, ('0 ' + input()).split())))
    C.append(list(map(int, ('0 ' + input()).split())))
    # C = [[list(map(int, input().split()))] for i in range(3)]
    A = [0] * 4
    B = [0] * 4

    for i in range(101):
        A = new_A(i)
        if check(A):
            return print('Yes')

main()
