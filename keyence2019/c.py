N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def m():
    if sum(A) < sum(B):
        return -1
    f = 0
    for i in range(N):
        if B[i] > A[i]:
            f = 1
    if f == 0:
        return 0


    C = [A[i]-B[i] for i in range(N)]
    org = [A[i] - B[i] for i in range(N)]
    C.sort(reverse=True)
    org.sort(reverse=True)

    def swapsum(plus, minus):
        if abs(C[plus]) > abs(C[minus]):
            C[plus] += C[minus]
            C[minus] = 0
        else:
            C[minus] += C[plus]
            C[plus] = 0
    ans = 0
    left = 0
    right = N-1
    while C[right] < 0:
        if -C[left] == C[right]:
            swapsum(left, right)
        else:
            swapsum(left,right)
        if C[left] == 0:
            left += 1
            ans += 1
        if C[right] == 0:
            right -=1
            ans +=1
    if org[left] == C[left]:
        return ans
    else:
        return ans+1

print(m())