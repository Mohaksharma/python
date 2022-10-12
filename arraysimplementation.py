#this is implementation of arrays using python
#learn to implement arrays
class Array(object):
    '''
    sizeofArray: means the total size of the array i.e initialized
    arrayType: means the data type of the array(all elements have to be of the same type)
    arrayItems: means the values at respective postion of array
    '''    
    def __init__(self,sizeofArray, arrayType = int):
        self.sizeofArray = len(list(map(arrayType,range(sizeofArray))))
        self.arrayItems = [arrayType(0)]*sizeofArray # initialize array with zeroes
        self.arrayType = arrayType

    def __str__(self):
        return ' '.join([str(i) for i in self.arrayItems])
    
    def __len__(self):
        return len(self.arrayItems)
    
    def __setitem__(self,index,data): #method to enable indexing
        self.arrayItems[index] = data
    
    def __getitem__(self,index):
        return self.arrayItems[index]
    
    def search(self, keytosearch):
        for i in range(self.sizeofArray):
            if self.arrayItems[i] == keytosearch:
                return 1
        return -1
    
    def insert(self,keytoinsert,position):
        if self.sizeofArray > position:
            for i in range(self.sizeofArray-2,position-1,-1):
                self.arrayItems[i+1] = self.arrayItems[i]
                self.arrayItems[position] = keytoinsert
        else:
            print('Array size is ',self.sizeofArray)
    
    def delete(self,keytodelete,position):
        if self.sizeofArray > position:
            for i in range(position,self.sizeofArray-1):
                self.arrayItems[i] = self.arrayItems[i+1]
                self.arrayItems[i+1] = self.arrayType(0)
        else:
            print('Array size is ',self.sizeofArray)
    def printitem(self,index):
        return self.arrayItems[index]

if __name__ == '__main__':
    a = Array(10,int)
    a.insert(2,2)
    a.insert(3,1)
    a.insert(4,7)
    print(len(a))
    print(a.printitem(1))
