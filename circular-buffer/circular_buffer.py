#class BufferFullException(BufferError):
    #"""Exception raised when CircularBuffer is full.

    #message: explanation of the error.

    #"""
    #def __init__(self, message):
        #pass


#class BufferEmptyException(BufferError):
    #"""Exception raised when CircularBuffer is empty.

    #message: explanation of the error.

    #"""
    #def __init__(self, message):
        #pass


#class CircularBuffer:
    #def __init__(self, capacity):
        #pass

    #def read(self):
        #pass

    #def write(self, data):
        #pass

    #def overwrite(self, data):
        #pass

    #def clear(self):
        #pass

#As per the exercise data, the newer elements get appended after the last element element added. This can be achieved by modelling the buffer as a list. So ae empty list is initialised for the buffer
#In the write operation, the capaity of the buffer is checked first. If the buffer is filled, exception must be raised to indicate that no further element can be added. Else the latest element is to appended after the last added element i.e. the leftmost element in the list is the oldest elment in the list while the leftmost element in the list is the oldest elment in the list. This is done by appending latest element to the end of the list using append() function
#In the read operation, the buffer capacity is first checked. If it is empty, then exception must be raised to indicate that no read operation is possible. If the buffer is non-empty, then two operations are done. First operation is the returning of the oldest element in the buffer i.e. the leftmost element in the list. This is done by storing the oldest element in a variable. The second operation is the removal of the oldest element in the buffer i.e. the leftmost element in the list which is done by slicing.
#In the overwrite operation, the buffer capacity is first checked. If the buffer is not full, the overwrite operation is same as the write operation i.e. newest element is added to the the last position using append() function. If the buffer is full, then the oldest element is replaced by the new element which now becomes the latest element. This can be done by removing the oldest element from the buffer(i.e. leftmost element from the list) using slicing operation and adding the overwiring value as the latest element in the buffer(i.e. rightmost element in the list) using append() function
#In the clear operation, all the elements in the buffer ar cleared using clear() function
class BufferFullException(BufferError):

    def __init__(self, message):
        self.message = message

class BufferEmptyException(BufferError):

    def __init__(self, message):
        self.message = message

class CircularBuffer:
    
    def __init__(self, capacity):
        self.capacity = capacity #Creates the attribute 'capacity' of the class instance for the capacity of the buffer
        self.buffer = [] #Creates the attribute 'buffer' of the class instance for the buffer which is an empty list
        self.reed = [] #Creates the attribute 'reed' of the class instance which is an empty list
        
    def read(self):
        if len(self.buffer) == 0: #Checks whether the buffer is empty
            raise BufferEmptyException("Circular buffer is empty") #Raises exception when buffer is empty
        else:
            self.reed = [self.buffer[0]] #Stores the oldest element in a list
            self.buffer = self.buffer[1:] #Removes the oldest element from the buffer
            return self.reed[0] #Returns the oldest element
            
    def write(self, data):
        if len(self.buffer) == self.capacity: #Cheks whether the buffer is full
            raise BufferFullException("Circular buffer is full") #Raises exception when buffer is full
        else:
            self.buffer.append(data) #Appends the element to the end of the list 

    def overwrite(self, data): 
        if len(self.buffer) < self.capacity: #Cheks whether the buffer is full
            self.buffer.append(data) #Appends the overwriting element to the end of the list
        else:
            self.buffer = self.buffer[1:] #Removes the oldest element from the list
            self.buffer.append(data) #Appends the overwriting element to the end of the list
        
    def clear(self):
        return self.buffer.clear() #Clears the buffer
