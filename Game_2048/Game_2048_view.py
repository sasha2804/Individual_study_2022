import tkinter as tk
from tkinter import *


class View(tk.Frame):
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        tk.Frame.__init__(self)
        self.master.bind_all('<Key>', controller.keyPressed)
        self.newGame = 0
        self.master.bind()
       
 
    def testCom(self):
        #print('testcom')
        self.controller.newGamePressed()

    def start(self, matrix, score):
        print('matrix: ',matrix)
        print('start')     
               
        self.root.geometry('400x530')
        self.root.resizable(height = False, width = False)
        
        scoreLabelTop= Label(text='score', bg='#ede0c8').place(x=205, y=10, width=190, height=25)
        scoreLabelBottom= Label(text=score, bg='#ede0c8', font=24).place(x=205, y=35, width=190, height=25)
        
        Frame(width = 90,height = 120).grid(row=0, column=0)
        gameName= Label(text='2048', font = 12).place(x=10, y=10, width=150, height=50)
        
        buttonNewGame = Button(bg='#f65e3b', text='New Game', command = self.testCom)
        #buttonNewGame.bind('<LButton>', self.testCom())
        
        buttonNewGame.place(x=205, y= 80, width=205, height=25)
        #command=self.controller.newGamePressed()
        
        #buttonNewGame.config(command=self.change)
        
        #buttonNewGame.config(command=None)
        
        #frame = Frame(bg = '#776e65',width = 90,height = 90)
        for i in range(4):            
            for j in range(4):
                frame = Frame(bg = '#776e65',width = 90,height = 90).grid(row=2+i, column=j, padx=5, pady=5)
                
        for i in range(4):            
            for j in range(4):
                label = Label(frame, text=matrix[i][j],bg = '#776e65',font = 12).grid(row=2+i, column=j, padx=5, pady=5)        
       
        self.mainloop()
    
         


    def interface(self, matr):        
        #self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cellFrame = tk.Frame(
                self.mainGrid,
                bg = '#DD5F12',
                width = 50,
                height = 50
                )
                cellFrame.grid(row = i, column = j, padx = 5, pady = 5)
                cellNumber = tk.Label(self.mainGrid, text = matr[i][j])
                cellNumber.grid(row = i, column = j)
                cellData = {'frame': cellFrame, 'number': cellNumber}
                #text = tk.Text(height = 18)
                #sample_text.pack()                
                row.append(cellData)
            self.cells.append(row)

    
    def updateGUI(self, matrix, score):
        scoreLabelBottom= Label(text=score, bg='#ede0c8', font=24).place(x=205, y=35, width=190, height=25)
        for i in range(4):            
            for j in range(4):
                frame = Frame(bg = '#776e65',width = 90,height = 90).grid(row=2+i, column=j, padx=5, pady=5)
                
                
        for i in range(4):            
            for j in range(4):
                label = Label(frame, text=matrix[i][j],bg = '#776e65',font = 12).grid(row=2+i, column=j, padx=5, pady=5)         
      


