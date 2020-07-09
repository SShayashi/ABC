from collections import deque
def m():
    S = input()
    N = len(S)

    q = deque(S)
    ans = 0
    while len(q) > 1:
        left,right = q[0], q[-1]
        if left == right:
            q.pop()
            q.popleft()
            continue
        if left == 'x':
            q.popleft()
            ans +=1
            continue
        if right == 'x':
            ans +=1
            q.pop()
            continue
        return -1
    return ans


print(m())