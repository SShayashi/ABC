def m():
    n = int(input())
    nowt, nowa = map(int, input().split())
    for _ in range(n-1):
        t, a = map(int, input().split())
        if t == a:
            nowt = max(nowt, nowa)
            nowa = max(nowt, nowa)
        elif t > a:
            if nowa < a:
                nowa = a
                nowt = int(nowa * (t / a))
                continue

            if nowt > nowa:
                if nowt < t:
                    nowt = t
                    nowa = int(nowt * (a / t))
                    continue

                nowa = int((a / t) * nowt)
                continue

            for i in range(nowa):
                if nowa < i * a:
                    nowa = i*a
                    break
            nowt = int(nowa * (t / a))
        else:
            if nowt < t:
                nowt = t
                nowa = int(nowt * (a / t))
                continue

            if nowa > nowt:
                if nowa < a:
                    nowa = a
                    nowt = int(nowa * (t / a))
                    continue
                nowt = int((t / a) * nowa)

                continue

            for j in range(nowt):
                if nowt < j * t:
                    nowt = j * t
                    break
            nowa = int(nowt * (a / t))
    return nowa + nowt


def ans():
    n = int(input())
    nowt, nowa = 1,1
    for _ in range(n):
        t, a = map(int, input().split())
        c = max(nowt//t,nowa//a)
        if nowt > c * t or nowa > c * a:
            c += 1
        nowt, nowa = max(c*t,t), max(c*a,a)
    return int(nowa+nowt)

print(ans())
