# 全通りを計算する
# collectins.conbination 1-19，len = 19の配列用意
# その中から9個選ぶ
# それぞれの選ばれたものを仕切りと考え，左の仕切りから順に1~10まで数える．
# それらを配列とみなす．
# それで全探索し，最も得点が高いものの組み合わせが答え
# 19C9 は3万程度なのでOK

import itertools


def main():
    n, m, q = map(int, input().split())

    A, B, C, D = [], [], [], []
    for _ in range(q):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    if m == 1:
        return sum(D)
    ans = 0
    length = m+n-1
    for item in itertools.combinations(range(length), m-1):
        ptn = []
        num = 1
        p = 0
        for i in range(length):
            if i == item[p]:
                num += 1
                p += 1
                p = min(m-2, p)
                continue
            ptn.append(num)
        tmp = 0
        for k in range(q):
            if (ptn[B[k]-1] - ptn[A[k]-1]) == C[k]:
                tmp += D[k]

        ans = max(tmp, ans)
    return ans

print(main())
