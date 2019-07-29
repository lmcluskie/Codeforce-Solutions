n=input()
lst = input().split()
lst = [int(i)%2 for i in lst]
if lst.count(0)==1:
    print(lst.index(0) + 1)
else:
    print(lst.index(1) + 1)