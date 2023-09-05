#class Node:
    #def __init__(self, value):
        #pass

    #def value(self):
        #pass

    #def next(self):
        #pass

#class LinkedList:
    #def __init__(self, values=[]):
        #pass

    #def __len__(self):
        #pass

    #def head(self):
        #pass

    #def push(self, value):
        #pass

    #def pop(self):
        #pass

    #def reversed(self):
        #pass

#class EmptyListException(Exception):
    #pass


class Node:
    def __init__(self, value):
        self.val = value
        self.nex = None

    def value(self):
        return self.val

    def next(self):
        return self.nex

        
class Node:
    def __init__(self, value, next=None):
        self.stored_value = value
        self.next_node = next
    def value(self):
        return self.stored_value
    def next(self):
        return self.next_node
class LinkedList:
    def __init__(self, values=[]):
        self.storage = []
        for value in values:
            self.push(value)
    def __len__(self):
        return len(self.storage)
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.storage) == 0:
            raise StopIteration
        return self.pop()
    def head(self):
        if len(self.storage) == 0:
            raise EmptyListException("The list is empty.")
        return self.storage[-1]
    def push(self, value):
        next_node = None
        if len(self.storage) > 0:
            next_node = self.head()
        self.storage.append(Node(value, next_node))
    def pop(self):
        if len(self.storage) == 0:
            raise EmptyListException("The list is empty.")
        return self.storage.pop().value()
    def reversed(self):
        return reversed(list(self))
        
class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
