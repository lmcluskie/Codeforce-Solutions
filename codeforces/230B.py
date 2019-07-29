_ = input()
numbers = [int(i) for i in input().split()]

limit = 10**6
tprimes = set()
lst = [1] * limit
for i in range(2, limit):
    if lst[i]:
        tprimes.add(i * i)
        for j in range(i * i, limit, i):
            lst[j] = 0

for num in numbers:
    print(['NO','YES'][num in tprimes])

print('Time: ', t1 - t0)