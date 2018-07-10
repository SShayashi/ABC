def m():
    h, w = map(int, input().split())
    a = [list(("."+input()+".")) for _ in range(h)]
    a.insert(0, ['.' for _ in range(w+2)])
    a.insert(h+1, ['.' for _ in range(w+2)])
    for i in range(1,h+1):
        for j in range(1,w+1):
            if a[i][j] != "#":
                continue
            if a[i+1][j] == "#":
                continue
            if a[i][j+1] == "#":
                continue
            if a[i-1][j] == "#":
                continue
            if a[i][j-1] == "#":
                continue
            return "No"
    return "Yes"

print(m())