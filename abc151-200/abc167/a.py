s = input()
t = input()
if t[:len(s)] == s and len(t) == len(s) +1:
    print('Yes')
else:
    print('No')
