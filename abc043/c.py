
def m():
    def cost(x,y):
        return (x-y) ** 2
    n = int(input())
    a = list(map(int, input().split()))
    ans = 99999999
    for y in range(-100, 101):
        c = 0
        for x in a:
            c += cost(x,y)
        ans = min(ans, c)
    return ans

print(m())