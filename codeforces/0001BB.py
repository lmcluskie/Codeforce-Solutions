n = int(input())
cells = [input() for i in range(n)]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha2 = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
nums = '0123456789'

for cell in cells:
    if 'C' in cell:
        c_loc = next(cell.index(x) for x in cell if x in 'C')
        if next(cell.index(x) for x in cell if x in nums) < c_loc:
            col = int(cell[c_loc+1:])
            alphacol = ''
            while col:
                alphacol = alpha2[col%26] + alphacol
                if col%26:
                    col -= col%26
                else:
                    col -= 26
                col //= 26
            row = cell[1:c_loc]
            print(alphacol+row)
        else:
            row = ''.join([x for x in cell if x in nums])
            col = ''.join([x for x in cell if x in alphabet])
            colst = [(alphabet.index(col[-1-i])+1)*26**i for i in range(len(col))]
            col = 0
            for i in colst:
                col += i
            print('R'+row+'C'+str(col))
    else:
        row = ''.join([x for x in cell if x in nums])
        col = ''.join([x for x in cell if x in alphabet])
        colst = [(alphabet.index(col[-1-i])+1)*26**i for i in range(len(col))]
        col = 0
        for i in colst:
            col += i
        print('R'+row+'C'+str(col))