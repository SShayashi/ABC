def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    cnt = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                price = 500 * a + 100 * b + 50 * c
                if price == X:
                    cnt +=1

    print(cnt)

main()