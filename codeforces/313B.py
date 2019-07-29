line = input()
n = int(input())
queries = []
pairs = [0]
count = 0

for i in range(n):
    queries.append([int(i) for i in input().split()])    

for i in range(len(line)-1):
    if line[i]==line[i+1]:
        count+=1
    pairs.append(count)

for query in queries:
    print(pairs[query[1]-1]-pairs[query[0]-1])