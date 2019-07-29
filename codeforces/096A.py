s = input()

danger = False
danger0 = 0
danger1 = 0

for i in s:
    if i == '0':
        danger0 += 1
        danger1 = 0
    if i == '1':
        danger0 = 0
        danger1 += 1
    if danger0 >= 7 or danger1 >= 7:
        danger = True
        break
    
if danger:
    print('YES')
else:
    print('NO')