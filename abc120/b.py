a, b, k = map(int, input().split())

data = []

for i in range(1, max(a,b)+1):
    if a % i == 0 and b % i == 0:
        data.append(i)
data.sort(reverse=True)
print(data[k-1])