MOD = 1000000007

def m():
    N = int(input())
    if N == 1:
        return 3
    s = str(input())
    s2 = str(input())
    a = []
    past = s[0]
    point = 0
    while point < len(s):
        if s[point] == s[point+1]:
            a.append('y')
            point += 2
        else:
            a.append('x')
            point += 1

        if point == len(s) -1:
            a.append('x')
            break

    ans = 0
    if a[0] == 'x':
        ans = 3
    else:
        ans = 6

    for j in range(1, len(a)):
        if a[j-1] == 'x' and a[j] == 'x':
            ans *=2 % MOD
        elif a[j-1] == 'y' and a[j] == 'x':
            ans *=1 % MOD
        elif a[j-1] == 'x' and a[j] == 'y':
            ans *=2 % MOD
        elif a[j-1] == 'y' and a[j] == 'y':
            ans *=3 % MOD

    return ans % MOD
print(m())
# def someone_ans():
#     n=int(input())
#     a=input()
#     b=input()
#     c=[]
#     i=0
#     while i<n:
#         if i == n-1:
#             c.append(1)
#             i+=1
#         elif a[i] == a[i+1]:
#             c.append(0)
#             i +=2
#         else:
#             c.append(1)
#             i+=1
#
#     if c[0] ==0: count=6
#     else: count=3
#     for i in range(len(c)-1):
#         if c[i]==1:count*=2
#         elif c[i]==0 and c[i+1]==0: count*=3
#     return count % 1000000007


# print(someone_ans())
