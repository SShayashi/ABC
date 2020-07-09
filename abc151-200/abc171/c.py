import string


def m():
    N = int(input())
    a2z = string.ascii_lowercase
    ans = ''
    while N != 0:
        N -= 1
        ans = a2z[N % 26] + ans
        N = N // 26
    return ans

print(m())
