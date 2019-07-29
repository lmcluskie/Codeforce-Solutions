n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)
    
for j in words:
    if len(j)>10:
        j = (j[0] + str(len(j)-2) + j[-1])
    print(j)
    