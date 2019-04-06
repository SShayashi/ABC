n = int(input())
a = list(map(int, input().split()))
def m():
    evens = []
    odds = []
    for i in a:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    evens_cnt = len(evens)
    odds_cnt = len(odds)
    if abs(evens_cnt - odds_cnt) <= 1:
        return 0

    if evens_cnt > odds_cnt:
        evens.sort(reverse=True)
        return sum(evens[odds_cnt+1:])
    else:
        odds.sort(reverse=True)
        return sum(odds[evens_cnt+1:])

print(m())