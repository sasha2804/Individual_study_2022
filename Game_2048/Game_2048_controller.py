from Game_2048_model import Matrix
from Game_2048_view_QT import View

class Controller:
    def __init__(self):
        self._model = Matrix()
        self.view = View(self)
        self.view.start(self._model.getMatrix(),self._model.getScore())      
        

    def keyPressed(self, event):
        self._model.turn(event.keysym)        
        self.view.updateGUI(self._model.getMatrix(),self._model.getScore())
        print('key pressed test')
    
    def newGamePressed(self):
        #pass
        #self.view.testCom(self)
        #self._model.createMatrix()
        print('test controller')
        #self._model.createMatrix()
        self._model.resetScore()
        self.view.updateGUI(self._model.getMatrix(),self._model.getScore())
        
        #self._model.turn(event.keysym)        
        #self.view.updateGUI(self._model.getMatrix(),self._model.getScore())        
        
    
        
        

if __name__ == '__main__':
    Controller()
    
    









