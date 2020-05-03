def m():
    X = int(input())
    length = 1001
    plus = [pow(i, 5) for i in range(0, length)]
    minas = [pow(i, 5) for i in range(-(length-1), 1)]
    minas.reverse()

    for i in range(length):
        for s in range(length):
            if (plus[i] - plus[s]) == X:
                return f'{i} {s}'

        for t in range(length):
            if (plus[i] - minas[t]) == X:
                return f'{i} {-t}'

    for i in range(length):
        for s in range(length):
            if (minas[i] - plus[s]) == X:
                return f'{-i} {s}'

        for t in range(length):
            if (minas[i] - minas[t]) == X:
                return f'{-i} {-t}'


print(m())
