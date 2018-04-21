def m():
    A, B, C, X, Y = map(int, input().split())
    ab = A + B
    cc = C * 2

    if ab > cc:
        if X == Y:
            return ((X + Y) // cc) * C
        if X > Y:
            d = X - Y
            price = (Y // cc) * C
            if A > cc:
                price += (d // cc) * 2 * C
                return price
            else:
                price += d * A
                return price
        else:
            d = Y - X
            price = (X // cc) * C
            if B > cc:
                price += (d / cc) * 2 * C
                return price
            else:
                price += d * B
                return price
    else:
        if X == Y:
            pass
        pass
    pass


def n():
    A, B, C, X, Y = map(int, input().split())
    ab = A + B
    cc = C * 2
    cost = 0
    if ab > cc:
        minn = min(X, Y)
        cost += minn * cc
    else:
        minn = min(X, Y)
        cost += minn * A + minn * B

    if X > Y:
        diff = X - Y
        aaa = A * diff
        ccc = cc * diff
        cost += min(aaa, ccc)
    else:
        diff = Y - X
        bbb = B * diff
        ccc = cc * diff
        cost += min(bbb,ccc)

    return cost


print(n())
