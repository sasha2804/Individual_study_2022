import random

class Matrix:
    def __init__(self):
        self.choice = {
            "Down": self.moveDown,
            "Up": self.moveUp,
            "Left": self.moveLeft,
            "Right": self.moveRight        
        }
        self.matrix = None
        self.width = 4
        self.height = 4
        self._status = 0 # check if it is NEEDED AT THE END
        self.score = 0 #add score after each update
        self.createMatrix()
        self.test = 'test'
        
    def resetScore(self):
        print('test reset score print')
        self.score = 0
        self.createMatrix()

    def createMatrix(self):      
        self.matrix = [[0 for i in range(self.width)]for j in range(self.height)]
        self.__checkStatus__()
        self.__checkStatus__()

    def __stack__(self):
        matrixTemp = [[0 for i in range(self.width)]for j in range(self.height)]
        for i in range(self.height):
            element = 0
            for j in range(self.width):
                if self.matrix[i][j] != 0:
                    matrixTemp[i][element] = self.matrix[i][j]
                    element += 1
        self.matrix = matrixTemp
        return self.matrix
    
    def __group__(self):
        for i in range(self.height):
            for j in range(self.width-1):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == \
                   self.matrix[i][j+1]:
                    self.score += self.matrix[i][j]*2
                    self.matrix[i][j] += self.matrix[i][j+1]
                    self.matrix[i][j+1] = 0
        return self.matrix
    
    def __reverse__(self):
        for i in self.matrix:
            i = i.reverse()
        return self.matrix
    
    def __transpose__(self):
        matrixTemp = [[0 for i in range(self.height)]for j in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                matrixTemp[i][j] = self.matrix[j][i]
        self.matrix = matrixTemp
        return self.matrix
    
    def __randomNum__(self):                  
        while True:
            i = random.randrange(0,4)
            j = random.randrange(0,4)
            if self.matrix[i][j] == 0:
                #rnd = random.choice([2,4])
                #self.matrix[i][j] = [rnd]
                self.matrix[i][j] = random.choice([2,2,2,2,2,2,2,2])
                break        

    def __checkStatus__(self):        
        zeroExists = 1
        maxIsReached = 1
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] == 0:
                    zeroExists = 2
                if self.matrix[i][j] >= 2048:
                    maxIsReached = 2
     
        if maxIsReached == 2:
            print('You won')
            self._status = 5
            return 5 # you won the game  
            
        elif zeroExists == 2:
            self.__randomNum__()
            self._status = 1
            return 1 # proceed the game
        elif zeroExists == 1:
            for i in range(self.height):
                for j in range(self.width-1):
                    if self.matrix[i][j] == self.matrix[i][j+1]:
                        self._status = 1
                        return 1 #proceed
            for i in range(self.height-1):
                for j in range(self.width):
                    if self.matrix[j][i] == self.matrix[j][i+1]:
                        self._status = 1
                        return 1 #proceed
            self._status = 2
            return 2 # lost
            
    def turn(self, direction):
        if direction in self.choice:
            self.choice[direction]()

    def moveRight(self):
        self.__stack__()
        self.__reverse__()
        self.__group__()
        self.__stack__()
        self.__reverse__()        
        self.__checkStatus__()    
    
    def moveLeft(self):
        self.__stack__()
        self.__group__()
        self.__stack__()
        self.__checkStatus__()    
    
    def moveUp(self):
        self.__transpose__()
        self.__stack__()
        self.__group__()
        self.__stack__()
        self.__transpose__()       
        self.__checkStatus__()            
    
    def moveDown(self):
        self.__transpose__()
        self.__stack__()
        self.__reverse__()
        self.__group__()
        self.__stack__()
        self.__reverse__()
        self.__transpose__()
        self.__checkStatus__()        
    
    def mprint(self):
        for i in self.matrix:
            pass
            #print(i)
    
    def getStatus(self):
        return self._status
    
    def getMatrix(self):
        return self.matrix
    
    def getScore(self):
        return self.score


    



#matr = Matrix()
#matr.createMatrix()
#matr.mprint()