N = int(input())
S = input()


def m():
    ans = 0
    left, right = 0, N
    black = 0
    white = 0
    tmp = '#'
    for i in range(N):
        if S[i] == '#':
            left = i
            break
    new_s = S[left:]
    prev = '#'
    for c in new_s:
        if c == '#' and prev == '#':
            black += 1
            prev = c
            continue

        if c == '.' and prev == '.':
            white += 1
            prev = c
            continue

        if c == '#' and prev == '.':
            white += 1
            prev = c
            continue

        if c == '.' and prev == '#':
            ans += min(black, white)
            black = 1
            white = 0
            prev = c
            continue
    ans += min(black, white)
    return ans

print(m())