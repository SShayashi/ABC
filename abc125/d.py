N = int(input())
A = list(map(int, input().split()))


def m():
    abs_A = [abs(a) for a in A]
    mines_cnt = 0
    for a in A:
        if a < 0:
            mines_cnt += 1
    if mines_cnt % 2 == 0:
        return sum(abs_A)
    return sum(abs_A) - min(abs_A)*2


print(m())
