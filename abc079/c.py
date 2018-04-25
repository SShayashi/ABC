def m():
    S = input()
    a, b, c, d = map(int, S)
    ope = [1, -1]
    sig_ope = ['+', '-']
    for w in range(2):
        for x in range(2):
            for y in range(2):
                ans = a + (b * ope[w]) + (c * ope[x]) + (d * ope[y])
                if ans == 7:
                    return "{0}{1}{2}{3}{4}{5}{6}=7".format(
                        a, sig_ope[w], b, sig_ope[x], c, sig_ope[y], d
                    )


print(m())
