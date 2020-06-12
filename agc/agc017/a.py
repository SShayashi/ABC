"""
奇数が一つでもあるとする．

それ以外の2**N-1 の組み合わせと，その奇数を選ぶか否かで
結果が奇数になるか偶数になるか操作できる．

P=0の，偶数の数を求めたい場合を考える．
2**N-1の数の組み合わせの中の一つに奇数があれば，ある奇数を選ぶ．
そうでない場合は，余っている奇数を選ばない．
というふうにすれば2**N-1の組み合わせすべてを偶数の数にすることができる．
よって答えは 2**N-1.

同様に奇数の場合も，ある奇数を選ぶか選ばないかで，選んだものの合計を奇数に固定できる．
よって，2**N-1

"""

def m():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    Even = [a for a in A if a % 2 == 0]
    Odd = [a for a in A if a % 2 == 1]
    if P == 1 and len(Odd) == 0:
        return 0

    if len(Odd) == 0:
        return pow(2, len(Even))
    else:
        return pow(2, N-1)


print(m())
