s = input()
zero_cnt = s.count('0')
one_cnt = s.count('1')
print(min(zero_cnt,one_cnt)*2)