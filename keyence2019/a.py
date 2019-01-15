def m():
    s = input().split()
    if '1' in s and '9' in s and\
        '7' in s and '4' in s:
        return 'YES'
    else:
        return 'NO'

print(m())