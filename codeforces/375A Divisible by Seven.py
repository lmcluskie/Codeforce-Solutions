import itertools as ite


def calcSum(arr1, arr2):
    aux = [a * b for a, b in zip(arr1, arr2)]
    return sum(aux) % 7


def main():
    cycle = [1, 3, 2, 6, 4, 5, 1, 3, 2, 6, 4, 5]
    tam = 6

    perm = [x for x in ite.permutations([1, 6, 8, 9])]

    num = input()
    res = []

    cnt = [0] * 10

    for c in num:
        cnt[ord(c) - ord('0')] += 1

    for c in "1689":
        cnt[ord(c) - ord('0')] -= 1

    idx = 0
    aux = 0
    for val in range(10):
        while (cnt[val] > 0):
            cnt[val] -= 1
            aux += val * cycle[idx % tam]
            aux %= 7
            idx += 1
            res.append(str(val))

    res = reversed(res);
    idx %= tam
    currArr = cycle[idx: idx + 4]
    sol = []
    solu = False
    for auxArr in perm:
        sumMod = calcSum(auxArr, currArr)
        if (sumMod + aux) % 7 == 0:
            sol = [str(x) for x in reversed(auxArr)]
            solu = True
            break

    if solu:
        sol.extend(res)
    else:
        sol = [0]

    stdout.write(str("".join(sol)))
    stdout.write("\n")


main()