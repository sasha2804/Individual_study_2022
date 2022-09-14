rowStart = 0
rowEnd = 6
colStart = 0
colEnd = 7
value = 1

ls = [[0 for i in range(colEnd)]for j in range(rowEnd)]

while colStart < colEnd and rowStart < rowEnd:
    for j in range(colStart, colEnd):
        ls[rowStart][j] = value
        value += 1
    rowStart += 1
    for p in range(rowStart, rowEnd):
        ls[p][colEnd - 1] = value
        value +=1
    colEnd -= 1
    if rowStart < rowEnd:
        for i in range(colEnd-1, colStart - 1, -1):
            ls[rowEnd-1][i] = value
            value += 1
        rowEnd -= 1
    if colStart < colEnd:
        for i in range(rowEnd - 1, rowStart - 1, -1):
            ls[i][rowStart-1] = value
            value += 1
        colStart += 1
 
for i in ls:
    print(i)
