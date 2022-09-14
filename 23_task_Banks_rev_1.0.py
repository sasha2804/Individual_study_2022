f = open('D:/=PYTHON=/Python_individual_study/Home_Work/banks_in.txt', 'r')
ls = f.readlines()
f.close()

lsInfo = ls[0].split(' ')
ls1Dim = int(lsInfo[0])
limit = int(lsInfo[1])

ls1 = [[0 for i in range(ls1Dim)]for j in range(ls1Dim)]
badBanks = set() #set for nonreliable banks adding


for row in ls[1:]:
    str1 = row.split(' ')
    for i in range(1,len(str1),2):
        if i == 1:
            ind = int(str1[i-1])
            ls1[ind][ind] = int(str1[i])
        else:
            ls1[ind][int(str1[i])] = float(str1[i+1])
print(ls1)

while True:
    needCheck = False
    for i in range(len(ls1)):
        if sum(ls1[i]) < limit and i not in badBanks:
            badBanks.add(i)
            needCheck = True
            for j in range(len(ls1)):
                ls1[j][i] = 0
            break
    if not needCheck:
        break
    
print(badBanks)











