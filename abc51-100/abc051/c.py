def m():
    sx, sy, tx, ty = map(int, input().split())
    X = tx-sx
    Y = ty-sy
    ans = ""

    # 一周
    ans += "U" * Y
    ans += "R" * X
    ans += "D" * Y
    ans += "L" * X

    # 左に一つずらして目的地まで
    ans += "L"
    ans += "U" * (Y+1)
    ans += "R" * (X+1)
    ans += "D"

    # 右にずれて開始地点まで
    ans += "R"
    ans += "D" * (Y+1)
    ans += "L" * (X+1)
    ans += "U"

    return ans


print(m())