def collatz(limit):
    maxc = 0
    maxn = 0
    for n in range(1, limit+1, 2):
        steps = 0
        i = n
        while i != 1:
            steps += 1
            if i%2 == 0:
                i /= 2
            else:
                i = 3*i + 1
        if steps > maxc:
            maxn = n
            maxc = steps
    return maxn, maxc

print(collatz(1000000))