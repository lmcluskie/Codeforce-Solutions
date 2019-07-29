n = int(input())
angles = []
for i in range(n):
    angles.append(int(input()))

for ang in angles:
    print(['NO','YES'][360%(180-ang)==0])
    