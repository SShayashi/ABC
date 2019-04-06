def m():
    A = []
    for _ in range(5):
        a = int(input())
        A.append(a)
    k = int(input())

    B = A.copy()
    for i in range(5):
        for j in range(i, 5):
            if B[j]-A[i] > k:
                return ':('
    return 'Yay!'

print(m())
