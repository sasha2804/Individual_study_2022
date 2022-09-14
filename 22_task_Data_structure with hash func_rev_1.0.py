
class Set:
  
    def __init__(self, size=10):
        self._size = size #size definition
        self.fill = 0 #filling degree definition
        self.arr = [None for _ in range(self._size)]  #list definition
   
    def _hashFunc(self, data): #hash function
        if isinstance(data, int):
            return data % self._size
        elif isinstance(data, float):
            return hash(data)%self._size
        elif isinstance(data, str):
            num = 0
            mult = 51
            for i in data:
                num = num*mult + ord(i)    
            return num % self._size

    def search(self, data):
        if data == None:
            raise Exception('None cannot be searched, enter valid request')
        index = self._hashFunc(data)
        while self.arr[index] != None:
            if self.arr[index] == data:
                print('Set contains: "{}"'.format(data))
                return True
            index += 1
        print('Set does not contain "{}"'.format(data))
        return False
     
    def addData(self, data):
        if data == None:
            raise Exception('None cannot be searched, enter valid request')        
        if self.fill * 2 > self._size:
            self.resize()
        index = self._hashFunc(data)
        while self.arr[index] not in (data, None):
            index = (index + 1)%self._size
        if self.arr[index] == None:
            self.arr[index] = data
            self.fill += 1
    
    def removeData(self, data):
        index = self._hashFunc(data)
        trig = False  
        
        if self.arr[index] == data:
            self.arr[index] = None
            if self.arr[index+1] != None:
                trig = True
        else:
            while self.arr[index+1] != None:
                index += 1
                if self.arr[index] == data:
                    self.arr[index] = None
                    trig = True
                    break
                
        while trig == True and self.arr[index+1] != None:
            data = self.arr[index+1]
            self.arr[index+1] = None
            self.fill -= 1
            self.addData(data)
            index += 1
        
        return trig
          
    def resize(self):
        tempSet = Set(self._size * 2)
        for i in range(self._size):
            if self.arr[i] != None:
                tempSet.addData(self.arr[i])
        self.arr = tempSet.arr
        self._size = tempSet._size
        self.fill = tempSet.fill
             
    def print(self): #function that prints results
        print(self.arr)
        #print(len(self.arr))
    
    
  

st = Set()

st.addData(3)
st.addData(4)
st.addData(13)
st.addData(14)
st.addData(23)
st.addData(103)
st.addData(104)
st.addData(203)
st.addData(204)
st.addData('24')
st.addData('terterttr')
st.print()
#st.search(14)
#st.removeData(13)
#print('remove: ',st.removeData(3))
st.print()




