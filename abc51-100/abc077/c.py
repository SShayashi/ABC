def m():
    def max_count(i, array):
        low = 0
        high = len(array) - 1
        middle = (low + high) // 2
        while (low <= high):
            if low == high:
                if i < array[middle]:
                    return len(array) - middle
                else:
                    return middle
            if i == array[middle]:
                return len(array) - middle
            elif i > array[middle]:
                low = middle + 1
            elif i < array[middle]:
                high = middle - 1
            middle = (low + high) // 2
        return len(array) - (low)

    def min_count(i, array):
        low = 0
        high = len(array) - 1
        middle = (low + high) // 2
        while (low <= high):
            if i == array[middle]:
                return middle
            elif i > array[middle]:
                low = middle + 1
            elif i < array[middle]:
                high = middle - 1
            middle = (low + high) // 2
        return low

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    cnt = 0
    A.sort()
    C.sort()
    for b in B:
        mmmc = min_count(b, A)
        maac = max_count(b, C)
        cnt += mmmc * maac
    return cnt


def someone_ans():
    def binary_search(L, key, mode):
        low, high = 0, len(L)
        mid = len(L) // 2
        while low <= high - 1:
            if L[mid] < key and mode == 0 or L[mid] <= key and mode == 1:
                low = mid + 1
            else:
                high = mid
            mid = (low + high) // 2
        return high

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    C.sort()
    ans = 0
    for i in B:
        Ai = binary_search(A, i, 0)
        Ci = len(C) - binary_search(C, i, 1)
        ans += Ai*Ci
    return ans


# print(m())
print(someone_ans())
