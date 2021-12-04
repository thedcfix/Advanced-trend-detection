import numpy

# queue containing DIM elements
class Queue:
    def __init__(self, dim):

        self.items = []
        self.dim = dim
	
    def put(self, el):

        if len(self.items) == self.dim:
            self.items = self.items[1 :]
        self.items.append(el)
	
    def clear(self):

        del self.items[:]
        self.dim = 0
		
    def changeSize(self, dim):

        self.dim = dim
		
    def show(self):

        print(self.items)
    
    def get(self):

        return numpy.array(self.items)
    
    def isFull(self):

        return len(self.items) == self.dim