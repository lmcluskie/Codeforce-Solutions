_ = input()
numbers = [int(i) for i in input().split()]
flip = []
gain = 0
for n in numbers:
    if n == 0:
        gain+=1
    elif gain>0:
        gain-=1    
    flip.append(gain)
    
print([numbers.count(1)+max(flip),numbers.count(1)-1][max(flip)==0])