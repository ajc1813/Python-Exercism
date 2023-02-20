#class Robot:
    #def __init__(self):
        #pass

#Random strings can be generated in python using random.choices() function. As mentioned in the exercise first two elements of the name are uppercase letters and remaining three elements of the name are digits. So a randon string using two uppercase letters and another random string using three digits are formed and then they are concatenated. This is converted into string using join() function. Reseting menas assigning a new random name to the robot which can be done using the same method mentioned above. But if the same method is used directly, same name will get alloted. To assign a new random name, seed() function is first used and then above methos is used
import string
import random
import re

class Robot:
    def __init__(self):
        self.name=''.join(random.choices(string.ascii_uppercase, k=2)+random.choices(string.digits, k=3)) #Creates a random name
        
    def reset(self):
        random.seed() #Initializes the random number generator
        self.name=''.join(random.choices(string.ascii_uppercase, k=2)+random.choices(string.digits, k=3)) #Creates a new random name


    
    
