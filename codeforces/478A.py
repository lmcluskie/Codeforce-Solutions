c = [int(i) for i in input().split()]
print([-1,sum(c)//len(c)][sum(c)%len(c)==0 and sum(c)!=0])