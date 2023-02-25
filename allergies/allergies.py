#class Allergies:

    #def __init__(self, score):
        #pass

    #def allergic_to(self, item):
        #pass

    #@property
    #def lst(self):
        #pass
#A dictionary is created first in which each key-value pair represent a value and allergin corresponding to it
#An attribute instance is created whose value is equal to the score when score is less than or equal to 256 and equal to the difference between score and 256 if score is greater than 256
#The values corresponding to allergens are all multiples of 2. So the score is expressed as sum of powers of 2 so that corresponding to each value, allergent can be obtained from the dictionary. For this a list powers of 2 that forms the score is created
#Now check whether length of list of powers of 2
#If it is zero, it means that person has no allergic item
#Else a list allergens associated with the person is formed. This is obtained by adding allergens corresponding to elements in list of powers of 2 to a list. The given item searched in the list of allergens
#The list of allergens is also returned

import math
allergens={1:'eggs',
           2:'peanuts',
           4:'shellfish',
           8:'strawberries',
           16:'tomatoes',
           32:'chocolate',
           64:'pollen',
           128:'cats'} #Creates a dictionary indicating allergens and corresponding values

class Allergies:
    
    def __init__(self, score):
         
        if score<=256: #Checks whether the score is less than or equal to 256
            self.score=score #Intiates an instance property for score
        else:
            self.score=score-256

        self.values=[] #Intializes an empty list for the powers of 2 that form the score
        while self.score>0: #Checks whether the instance property for score is greater than zero
            power = int(math.log(self.score, 2))
            self.score = self.score - 2**power
            self.values+=[2**power]
            
    def allergic_to(self, item):
        if len(self.values)==0:
            return False
        else:
            allergic_list=[allergens[value] for value in self.values] #Forms the allergens associated with a person
            return item in allergic_list
        
    @property
    def lst(self):
        allergic_list=[allergens[value] for value in self.values] #Forms the allergens associated with a person
        return allergic_list
