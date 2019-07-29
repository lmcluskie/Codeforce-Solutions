ncnt = int(input())
n = [int(i) for i in input().split()]
n.sort()
mcnt = int(input())
m = [int(i) for i in input().split()]
m.sort()

matches = 0

for boy in n:
    for girl in m:
        if abs(boy-girl)<=1:
            matches += 1 
            m.remove(girl)
            break

print(matches)