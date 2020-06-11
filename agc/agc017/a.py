def m():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    Even = [a for a in A if a % 2 == 0]
    Odd = [a for a in A if a % 2 == 1]
    import itertools
    if P == 0:
        even_cnt = len(Even) * (len(Even)+1) // 2
        odd_cnt = 0
        for i in range(1, len(Odd)+1, 2):
            odd_cnt += len(list(itertools.combinations(Odd, i)))
        return max(even_cnt,1) * max(1, odd_cnt)
    else:
        even_cnt = odd_cnt = 0
        for i in range(1, len(Odd)+1, 2):
            odd_cnt += len(list(itertools.combinations(Odd, i)))
        for i in range(0, len(Even)+1, 2):
            even_cnt += len(list(itertools.combinations(Even, i)))
        return max(1,even_cnt)*max(1,odd_cnt)


print(m())
