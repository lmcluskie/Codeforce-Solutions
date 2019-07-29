first = input()
second = input()

nk = first.split()
nk = list(map(int, nk))
n = nk[0]
k = nk[1]-1

scores = second.split()
scores = list(map(int, scores))

count = 0

for i in scores:
    if i >= scores[k] and i>0:
        count+=1
    else:
        break
    
print(count)  