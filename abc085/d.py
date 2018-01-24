def answer():
    import sys
    input = sys.stdin.readline
    wield = 0
    l = []
    N, H = map(int, input().split())
    for i in range(N):
        a, b = map(int, input().split())
        l.append(b)
        wield = max(a, wield)
    l.sort(reverse=True)
    ret = 0
    for a in l:
        if H <= 0:
            break
        if a > wield:
            ret += 1
            H -= a
        else:
            break
    if H > 0:
        ret += (H + wield - 1) // wield
    print(ret)

def main():
    N, Y = [int(i) for i in input().split()]

    A = []
    B = []

    for i in range(N):
        a, b = [int(i) for i in input().split()]
        A.append(a)
        B.append(b)

    B.sort()
    B.reverse()
    A.sort()
    A.reverse()

    cnt = 0
    for i in range(1000000):
        if Y <= 0:
            print(int(cnt))
            return

        b_m = max(B, default=0)
        a_m = max(A)
        if b_m > a_m:
            b_cnt = B.count(b_m)
            # B.
            for z in range(b_cnt):
                B.remove(b_m)
            Y = Y - b_m * b_cnt
            cnt += b_cnt
        else:
            if Y % a_m == 0:
                c = int(Y / a_m)
                print(cnt + c)
                return
            else:
                c = int(Y / a_m)
                print(cnt + c + 1)
                return
# main()

answer()