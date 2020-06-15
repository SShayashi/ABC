def m():
    MOD = 998244353
    N = int(input())
    D = [0] + list(map(int, input().split()))
    if D[1] != 0:
        return 0
    tree = {1:1}
    for i in range(2, N + 1):
        if D[i] == 0: return 0
        tree[D[i] + 1] = tree[D[i] + 1] + 1 if tree.get(D[i] + 1, False) else 1

    height = len(tree.keys())+1
    cnt = 1
    for i in range(2, height):
        if not tree.get(i, 0):
            return 0
        cnt = cnt * pow(tree[i-1], tree[i]) % MOD
    return cnt


print(m())
