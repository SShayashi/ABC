def main():
    x, y = map(int, input().split())
    if x % y == 0:
        return print('-1')
    for i in range(1000000000):
        if (i * x) % y != 0:
            return print(i*x)
main()
