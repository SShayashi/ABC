def main():
    A, B, C = map(int, input().split())
    m = [A,B,C]
    m.sort(reverse=True)
    d = (m[0] - m[1]) + (m[0] - m[2])
    if d % 2 == 0:
        print(d//2)
    else:
        print((d//2)+2)

main()
