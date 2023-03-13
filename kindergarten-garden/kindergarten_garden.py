#class Garden:
    #def __init__(self, diagram, students):
        #pass
#Two dictionaries are defined. One is dictionary for plants in which each key-value pair represnets a letter and the plant associated with that letter. Second dictionary for students in which each key-value pair represent a student and  number associated with the student
#The class 'Garden' has two arguements namely 'diagram' and 'students'
#In the tests, either one arguement is passed or two arguements are passed. Examples are 'garden = Garden("RC\nGG")' and 'garden = Garden("VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"]'. In the first example, no value is passed for the 'students' arguement and in the second example value is passed for 'students' arguement. In the first example TypeError will be present as value is not passed[TypeError: Garden.__init__() missing 1 required positional argument: 'students']. To avoid this, None is set as the default value of the 'students' arguement
#Two attributes for the class instance are created namely diagram and students. If the value of the 'students' arguement is None, then value of the attribute 'students' is same as that of the arguement 'students' else it is the list obtined after sorting the value of 'students' arguement which is a list
#In the test it is specified 'garden.plants("Alice")' which menas that a method 'plants' is required with an arguement
#As explained in the problem statement, each student is assigned four plants with two each in two rows.The newline character indicates the starting of the new row. So for finding the plants associated with student, a string of four characters are found in which the first two characters corresponds to plants associated with the student in the first row and last two characters corresponds to plants associated with the student in the second row
#First an empty list is created for the plants associated with the student
#For combining the plants associated with a student, the length of the garden is checked. If only one student is present, there will be only two elements each in two rows. As told earlier rows are seperated by newline character. So length of the garden is 5 if only one student is present else length will be greater than 5
#If only one student is present, the plants associated with him/her can be easily obtained by replcing the newline character with replace() function with null. This gives the string of all plants associated with the student. Then the plants corresponding to each letter in the string is obtained from the palnt dictionary and added to the list for plants associated with the student
#If only multiple students are present, the rows are joined by removing the newline character using a replace() function. Since corresponding to each student, there are two succesive characters in each row, a list is created in which each element are obtained by grouping two successive charcters of the string starting from the left end. The first half of the list corresponds to the upper row while second half corresoponds to the lower row. The list is divided into two halves and the corresponding elements are added. The result is a lsit in which each element is a string consisting of four charcaters corresponding to each student in alphabetical order. Now to find the plants associated with th student, the element corresponding to the student should be found. For this the index of the lement should be found. If the arguement 'student' has None value, then the value associated with the student is found from the dictionary for students else the index of the student in the sorted list is found. Using this index the element is chosed from the list for plants of all students is chosen. Then corresponding to each letter in the element, corresponding plant is obtained from the dictionary for plants and added to the list for plants associated with the student
import textwrap #Imports the textwrap module
from operator import add
plants_dict={
            'G':'Grass',
            'C':'Clover',
            'R':'Radishes',
            'V':'Violets'
            } #Creates a dictionary for plants
students_dict={
                'Alice':0,
                'Bob':1,
                'Charlie':2,
                'David':3,
                'Eve':4,
                'Fred':5,
                'Ginny':6,
                'Harriet':7,
                'Ileana':8,
                'Joseph':9,
                'Kincaid':10,
                'Larry':11
            } #Creates a dictionary for students
class Garden:
    def __init__(self, diagram, students=None):
        self.diagram=diagram #Creates the attribute 'diagram' of the class instance
        if students==None: #Checks whether the value of the arguement 'students' is None
            self.students=students #Creates the attribute 'diagram' of the class instance whose value is equal to the value of the arguement 'students'
        else:
            self.students=sorted(students) #Creates the attribute 'diagram' of the class instance whose value list obtained after sorting the list of the arguement 'students'

    def plants(self,student): #Creates the method 'plants'
        self.student=self.students
        plants_list=[] #Creates an empty list for the plants associted wiht the student
        if len(self.diagram)<=5: #Checks whether the length of the diagram/gaden is 5
            self.diagram=self.diagram.replace("\n","") #Joins the rows by replacing the newline character which will give the string of plants associated with the student
            for letter in self.diagram: #Iterates over the letters in the string
                plants_list+=[plants_dict[letter]] #Obtains the plant corresponding to the letter from the dictionary for plants and adds it to the list for plants associated with the student
            return plants_list
        else:
            self.diagram=self.diagram.replace("\n","") #Joins the rows by replacing the newline character
            diagram_list=textwrap.wrap(self.diagram, 2) #Creates a list from the string
            middle_index=int(len(diagram_list)/2) #Finds the middle index of the list
            upper_plant_row=diagram_list[:middle_index] #Obtains the upper row of the garden
            lower_plant_row=diagram_list[middle_index:] #Obtains the lower row of the garden
            full_plants_list = list(map(add, upper_plant_row, lower_plant_row)) #Performs element-wise addition
            if self.student==None: #Checks whether the value of the arguement 'student' is None
                student_index=students_dict[student] #Obtains value associated with the student from the dictionary for students
            else:
                student_index=self.students.index(student) #Obtains the index of the student from thesorted list
            student_plants=full_plants_list[student_index] #Finds the index of the element associated with the student
            for plant in student_plants: #Iterates over the letter in the element
                plants_list+=[plants_dict[plant]] #Adds the pants to the list for plants associated with thestudent
            return plants_list       