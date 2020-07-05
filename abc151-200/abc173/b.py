def m():
    N = int(input())
    S = [input() for _ in range(N)]
    import collections
    c = collections.Counter(S)
    print('AC x', c.get('AC', 0))
    print('WA x', c.get('WA', 0))
    print('TLE x',c.get('TLE', 0))
    print('RE x', c.get('RE', 0))

m()