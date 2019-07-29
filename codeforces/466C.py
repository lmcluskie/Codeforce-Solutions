n = int(input())
arr = [int(i) for i in input().split()]

total = sum(arr)
splits = 0
k = 0
l = 0
a = []
b = []

if total%3!=0:
    pass
else:
    for i in range(n):
        k+=arr[i]
        if k == total/3 and i!=n-1:
            a.append(i)
        if k == 2*total/3 and i!=n-1:
            b.append(i)
    for i in a:
        while l<len(b) and i>=b[l]:
            l+=1
        splits += len(b)-l
        
print(splits)