from Queue import *


###data reading and preparation block START###
f = open('D:/=PYTHON=/Python_individual_study/Home_Work/Islands_in.txt', 'r')
lsIn1 = f.readlines()
f.close()

#read dimensions of array
k = ''
lsDim = []

for i in range(len(lsIn1[0])):
    if lsIn1[0][i].isdigit():
        k += lsIn1[0][i]
    else:
        lsDim.append(int(k))
        k = ''   
print(lsDim)
width = lsDim[0]
height = lsDim[1]

#make list
ls = []
for i in range(1,width):
    ls1 = []
    for j in range(len(lsIn1[i])):
        if lsIn1[i][j].isdigit() == True:
            ls1.append(int(lsIn1[i][j]))    
    ls.append(ls1)
print(ls)     
###data reading and preparation block FINISH###


dls = DLinkedList()
checkedList = []
lsIslands = []
count = 0

for y in range(height):    
    for x in range(width):        
        if ls[y][x] == 1:
            lsIn = [y,x]
            dls.pushFront(lsIn)
                 
            while dls.getSize() > 0:
                lsOut = dls.popBack()
                if lsOut not in checkedList:
                    checkedList.append(lsOut)
                    count += 1
                y = lsOut[0]
                x = lsOut[1]
 
                if y + 1 < height and ls[y+1][x] == 1 and [y+1,x] not in checkedList:
                    lsIn = [y+1, x]
                    dls.pushFront(lsIn)               
                if x + 1 < width and ls[y][x+1] == 1 and [y,x+1] not in checkedList:
                    lsIn = [y, x+1]
                    dls.pushFront(lsIn)                   
                if  y - 1 >= 0 and ls[y-1][x] == 1 and [y-1, x] not in checkedList:
                    lsIn = [y-1, x]   
                    dls.pushFront(lsIn)                   
                if x - 1 >= 0 and ls[y][x-1] == 1 and [y,x-1] not in checkedList:
                    lsIn = [y, x-1]
                    dls.pushFront(lsIn)
                if dls.getSize() == 0 and count != 0:
                    lsIslands.append(count)
                    count = 0

if len(lsIslands) == 0:
    print('There are no islands')
else:
    factor = max(lsIslands)/min(lsIslands)         
    print('Unevennes factor: %.5f'%factor)                
                
#writing to file    
f1 = open('D:/=PYTHON=/Python_individual_study/Home_Work/Islands_out.txt', 'w+')
f1.write('Unevennes factor: %.5f'%factor)
f1.close()



            

                
                 
     
           
  
 
