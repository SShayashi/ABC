from collections import Counter


# def m():
#     n = int(input())
#     s = str(input())
#     ALL = [str(i) for i in range(10)]
#     d = [{} for _ in range(10)]
#     for ind, char in enumerate(ALL):
#         f = False
#         for k in range(n):
#             if s[k] == char: f = True
#             if not f: continue
#             d[ind] = dict(Counter(s[k + 1:]))
#             break
#     ans = set()
#     for i in range(10):
#         for a in ALL:
#             for b in ALL:
#                 tmp = d[i].copy()
#                 if len(tmp) == 0: continue
#                 if not tmp.get(a, 0): continue
#                 if not tmp.get(b, 0): continue
#                 tmp[a] -= 1
#                 tmp[b] -= 1
#                 if tmp[a] >= 0 and tmp[b] >= 0:
#                     ans.add(str(i) + a + b)
#     return len(ans)

def m2():
    n = int(input())
    s = str(input())
    ALL = [str(i) for i in range(10)]
    ans = 0
    for a in ALL:
        for b in ALL:
            for c in ALL:
                flag = 0
                for i in range(n):
                    if s[i] == a and flag == 0:
                        flag = 1
                        continue
                    if s[i] == b and flag == 1:
                        flag = 2
                        continue
                    if s[i] == c and flag == 2:
                        flag = 3
                    if flag == 3:
                        ans += 1
                        break
    return ans

print(m2())
