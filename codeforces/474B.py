from itertools import accumulate
import bisect

n = int(input())
piles = [int(i) for i in input().split()]
piles = list(accumulate(piles))

m = int(input())
worms = [int(i) for i in input().split()]

for worm in worms:
    print(bisect.bisect_left(piles,worm)+1)
