#  how many distinct values of (n r) for 1<=n<=100 are greater than one million where r <= n

import math

def choose(n, r):
    return math.factorial(n) / math.factorial(n-r) / math.factorial(r)

tally = 0
for i in range(1, 101):
    for j in range(1, i):
        answer = choose(i,j)
        print(i, j, answer)
        if answer > 1000000:
            tally += 1

print(tally)