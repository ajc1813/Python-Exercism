#class Cipher:
    #def __init__(self, key=None):
        #pass

    #def encode(self, text):
        #pass

    #def decode(self, text):
        #pass

import random
import string
class Cipher:
    def __init__(self, key=None):
        if key==None:
            self.key=''.join(random.choices(string.ascii_lowercase, k=100)) #Creates a random key when key is none
        else:
            self.key=key
       
    def encode(self, text):
        return "".join([chr(((ord(c) + ord(self.key[index % len(self.key)]) - 194) % 26) + 97)
                        for index, c in enumerate(text)])
    
    def decode(self, text):
        
        return "".join([chr(((ord(c) - ord(self.key[index % len(self.key)])) % 26) + 97)
                        for index, c in enumerate(text)])
            
        