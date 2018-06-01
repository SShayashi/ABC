def m():
    n = int(input())
    S = [str(input()) for _ in range(n)]
    march = [[] for _ in range(5)]
    for i in range(n):
        if S[i][0] == "M":
            march[0].append(S[i])
        elif S[i][0] == "A":
            march[1].append(S[i])
        elif S[i][0] == "R":
            march[2].append(S[i])
        elif S[i][0] == "C":
            march[3].append(S[i])
        elif S[i][0] == "H":
            march[4].append(S[i])

    cnt = 0
    for j in range(n):
        if len(march[j]) == 0:
            cnt +=1
    if cnt < 3:

        return 1

    if cnt == 3:
        pass

    if cnt == 4:
        pass

    if cnt == 5:
        pass

print(m())