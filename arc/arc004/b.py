"""
http://kyopro.hateblo.jp/entry/2019/05/23/214835

d[i]は並び替えても良い
最大の場合は直線に並べた場合でsum(d)
最小の場合は，max(d) - (sum(d) - max(d))= max(d)*2 - sum(d)
もし，これらが0を下回る場合は，max(d)を除くd[i]を使って0にたどり着くことが可能
理由：d[i]とd[i+1]の角度は自由に置くことができるので，d[i]，d[i+1]をつなげたときの0の距離pは
( d[i]-d[i+1] <= p <= d[i]+d[i+1]) の中から自由に選べる．
よって，sum[d]-max(d)がmax(d)を超えている場合，角度を調節して0までの距離を0にできる
一方で，sum[d]-max(d)よりもmax(d)が多い場合は，その差分が答えとなる


"""

def m():
    N = int(input())
    D = [int(input()) for _ in range(N)]
    ans1 = sum(D)
    ans2 = max(0, max(D)*2-ans1)
    print(ans1)
    print(ans2)

m()