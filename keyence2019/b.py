def m():
    S = input()
    a = 'keyence'
    x = 0
    if S[0] == 'k':
        for i in range(len(S)):
            if S[i] == a[x]:
                x += 1
                continue
            else:
                break
        if S[-7+x:] == a[-7+x:]:
            return 'YES'
        else:
            return 'NO'


    else:
        if a == S[-7:]:
            return 'YES'
        else:
            return 'NO'



print(m())