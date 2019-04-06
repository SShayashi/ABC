n = int(input())
a = list(map(int, input().split()))

def m():
    d = {}
    for i in a:
        if d.get(i, 0) == 0:
            d[i] = 1
        else:
            d[i] +=1
    for j in d.values():
        if j > 2:
            print('NO')
            return
    incres = []
    decres = []
    tmp = list(d.items())
    tmp.sort(key=lambda x:x[0])
    item = []
    for i in range(len(tmp)):
        k,v = tmp[i]
        item.append([k,v])

    for i in range(len(item)):
        k, v = item[i]
        incres.append(k)
        item[i][1] -= 1

    for j in reversed(range(len(item))):
        k, v = item[j]
        if v == 0:
            continue
        decres.append(k)

    def show_ans(array):
        if len(array) == 0:
            print('0')
            print('')
        else:
            print(len(array))
            for x in array:
                print(x, end='')
                print(' ', end='')
            print('')

    print('YES')
    show_ans(incres)
    show_ans(decres)

m()