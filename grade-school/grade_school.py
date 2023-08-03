#class School:
    #def __init__(self):

    #def add_student(self, name, grade):
        #pass

    #def roster(self):
        #pass

    #def grade(self, grade_number):
        #pass

    #def added(self):
        #pass

#The solution involves forming a dictionary and two lists
#In the dictionary keys are grades and key-values are students who obtained the grade(which means there can be multiple values corresponding to a grade). The dictionary should satisfy the condition is that a student is added only to one grade and only once to each grade. The dictionary is first sorted according to the keys i.e. grades and values of each keys should sorted alphabetically 
#One of the list has an entry 'True' corresponding to each student succesfully added to the dictionary which means that the student was not previously present as a key-value in the dictionary and 'False' corresponding to each student who was not added to the dictionary which means that the student was not previously present as a key-value in the dictionary
#Second list is a roaster of students in the order of the grades and soreted alphabetically within each grade. This list is obtained from the grade dictionary
#At first an empty list for holding student names is initialized
#If the student name is not present in the list of names two operations are done. First a 'True' is added to the list indicating whether student is successfully added or not or else 'False' is added. Second the student name and the grade is added to the dictionary of grades. But if the grade is already present in the dictionary, then it will be overwritten. To prevent this, first it is checked whether the grade is present or not in the dictionary. if grade is laready present, the student name is appended to the value of the key corresponding to the grade or else the grade and the student name is added as a new key-value pair to the dictionary. Then the dictionary elements are first sorted according to the keys(i.e. grades) and then values corresponding to each key(i.e. student names) are sorted alphabetically
#The roaster is obtained by forming a lsit of key-values of the grade dictionary. Since keys(i.e. grades) can have multiple key-values(i.e. names), the list obtained may be a nested list. This nested list is flattened using the sum() function

class School:
    def __init__(self):
        self.name_list=[] #Initilaises an empty list to store names of all students
        self.rawster = [] #Initilaises an empty list for roaster students
        self.aded = [] #Initilaises an empty list for displaying student is succesfully added or not
        self.graid = {} #Initilaises an empty dictionary for grades and associated students
        
    def add_student(self, name, grade):
        if name not in self.name_list: #Checks whether the student name is absent in the list of student names
            self.name_list.append(name) #Adds the student to the list of student names
            self.aded.append(True) #Adds 'True' to the list indicating whether student is successfully added or not
            if self.graid.get(grade) is None: #Checks grade is presesnt in the dictionary
                self.graid[grade] = [name] #Adds new key-value pair to the dictionary
            else:
                self.graid[grade] += [name] #Adds the student name to the grade
            self.graid = {key : sorted(self.graid[key]) for key in sorted(self.graid)} #Sort the dictionary elements first according to the keys(i.e. grades) and then values corresponding to each key(i.e. student names) are sorted alphabetically
        else:
            self.aded.append(False) #Adds 'False' to the list indicating whether student is successfully added or not
            
    def roster(self):
        self.rawster=list(self.graid.values()) #Obtains a list key-values which is a nested list
        self.rawster=sum(self.rawster, []) #Flattens the nested list
        return self.rawster #returns the student roaster
           
    def grade(self, grade_number):
        if len(self.graid) == 0: #Checks whether the dictionay is empty
            return [] #Returns an empty list(as per test data)
        else:
            if self.graid.get(grade_number) is None: #Checks whether the grade passed is None
                return [] #Returns an empty list(as per test data)
            else:
                return self.graid.get(grade_number) #Returns an list of students corresponding to the grade

    def added(self):
        return self.aded #Returns list indicating whether the student is succesfully added or not to the grade dictionary