import string
n = int(input())

def m():
    S = []
    for i in range(n):
        a = input()
        S.append(a)
    ans = []
    alf_dict = {}
    for c in string.ascii_lowercase:
        alf_dict[c] = 0
    def solve(s):
        d = alf_dict.copy()
        for c in s:
            if d.get(c, 0) == 0:
                d[c] = 1
            else:
                return 'No'
        tmp = list(d.items())
        tmp.sort(key=lambda x:x[0])
        alf = [k for k,v in tmp]
        val = [v for k,v in tmp]
        r = l = 0
        for i in range(len(val)):
            if val[i] != 0:
                l = i
                break

        for i in reversed(range(len(val))):
            if val[i] != 0:
                r = i
                break
        result = val[l:r+1]
        if 0 in result:
            return 'No'

        return 'Yes'
    for s in S:
        ans.append(solve(s))
    for x in ans:
        print(x)

m()