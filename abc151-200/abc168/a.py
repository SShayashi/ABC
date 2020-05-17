n = input()
if int(n[-1]) == 3:
    print('bon')
elif int(n[-1]) in (0,1,6,8):
    print('pon')
else:
    print('hon')