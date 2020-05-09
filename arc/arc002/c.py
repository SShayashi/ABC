def m():
    import itertools
    itertools.product()
    n = int(input())
    c = str(input())
    ans = float('inf')
    cmd = ('A', 'B', 'X', 'Y')
    for l1 in range(4):
        for l2 in range(4):
            for r1 in range(4):
                for r2 in range(4):
                    tmp = c
                    tmp = tmp.replace(cmd[l1] + cmd[l2], 'L')
                    tmp = tmp.replace(cmd[r1] + cmd[r2], 'R')
                    ans = min(ans, len(tmp))

    return ans



print(m())
