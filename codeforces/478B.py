ins = [int(i) for i in input().split()]
p,t = ins 

most = (p-t)*(p-t+1)//2
if t==1:
    least = most
else:
    least = (t-p%t)*(p//t-1)*(p//t)//2 + p%t*(p//t)*(p//t+1)//2
print(least,most)