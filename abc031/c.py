def m():
    n = int(input())
    a = list(map(int, input().split()))
    takahashi = -100
    # 高橋くん
    for i in range(n):
        aoki = -100
        index = -100
        # 青木くん
        for k in range(n):
            if i == k:
                continue
            if i > k:
                b = a[k:i+1]
                s = sum(b[1::2])
                if aoki < s:
                    aoki = s
                    index = k

            if i < k:
                b = a[i:k+1]
                s = sum(b[1::2])
                if aoki < s:
                    aoki = s
                    index = k
        if i > index:
            tmp = a[index:i+1]
            takahashi = max(takahashi,sum(tmp[::2]))
        else:
            tmp = a[i:index+1]
            takahashi = max(takahashi,sum(tmp[::2]))


    return takahashi


print(m())
