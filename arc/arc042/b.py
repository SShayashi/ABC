import math


def m():
    x, y = map(int, input().split())
    N = int(input())
    ans = 10 ** 7
    XY = [list(map(int, input().split())) for _ in range(N)]
    XY.append(XY[0])
    for i in range(1, N+1):
        px, py = XY[i - 1]
        cx, cy = XY[i]
        if (py - cy) == 0:
            d = abs(py - y)
            ans = min(ans, d)
            continue
        if (px - cx) == 0:
            d = abs(px - x)
            ans = min(ans, d)
            continue

        k = (py - cy) / (px - cx) if (px - cx) != 0 else 0
        b = cy - (cx * k)
        v_k = -(1 / k) if k != 0 else 0
        v_b = y - (v_k * x)
        v_x = (b - v_b) / (v_k - k)
        v_y = k * v_x + b
        d = math.sqrt((v_x - x) ** 2 + (v_y - y) ** 2)
        ans = min(d, ans)
        px, py = cx, cy
    return ans


print(m())
