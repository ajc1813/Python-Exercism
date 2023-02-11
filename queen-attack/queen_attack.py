#class Queen:
    #def __init__(self, row, column):
        #pass

    #def can_attack(self, another_queen):
        #pass

#Two attributes named 'row' and 'column' are first created for the class instance #Since chess board is represented by an 8 by 8 array, the valid values for row and column should be from 0 to 7. So next it is checked whether the values of the attributes row and column lies between 0 and 8. If not raise appropriate ValueError
#Next is the pre-defined instance method 'can_attack' in which 'another_queen' is given as the paramater
#Now consider the tests related to the instance method. An example is 'self.assertIs(Queen(1, 7).can_attack(Queen(0, 6)), True)'. Here we can see that '.can_attack()' following the class 'Queen' means that the instance method 'can_attack' is called. In that the parameter given is the class 'Queen' itself. This means that the parameter 'another_queen' is an object of the class 'Queen'. The attributes of an instance can be obtained by specifying the insyance followed by dot followed by the attribute name. So for obtaining 'row' attribute of the object 'another_queen', 'another_queen.row' is used. Similarly for obtaining 'column' attribute of the object 'another_queen', 'another_queen.column' is used
#In the instance method first it is checked whether both queens are in the same square
#If yes, then appropriate ValueError is raised
#If no, it is checked whether the queens are in the same row, column or diagonal. Queens are in the same row or column if their rows or columns are same respectively. Queens are in the same daigonal if the difference in values of their rows is equal to the difference in the values of their columns. For example positions (2, 2)and (3, 1) are in the same daigonal as their rows and columns differ by value 1. Similarly positions (2, 2) and (0, 4) are in same diagonal as change in row value and column value is 2. Here the difference can be positive or negative but only absolute value is considered. For obtaining absolute value, abs() function is used.


class Queen:
    def __init__(self, row, column):
        self.row=row #Creates the attribute 'row' for the class instance 
        self.column=column #Creates the attribute 'column' for the class instance 
        if self.row<0: #Checks whether the value of the attribut 'row' is less than 0
            raise ValueError("row not positive") #Raises ValueError
        elif self.row>7: #Checks whether the value of the attribut 'row' is greater than 7
            raise ValueError("row not on board") #Raises ValueError
        elif self.column<0: #Checks whether the value of the attribut 'column' is less than 0
            raise ValueError("column not positive") #Raises ValueError
        elif self.column>7: #Checks whether the value of the attribut 'column' is greater than 07
            raise ValueError("column not on board") #Raises ValueError

    def can_attack(self, another_queen):
        if ((self.row==another_queen.row) and (self.column==another_queen.column)): #Checks whether the queens are in the same square
            raise ValueError("Invalid queen position: both queens in the same square") #Raises ValueError
        else:
            row_diff=abs(self.row-another_queen.row) #Calculates the absolute difference of row values of queens
            column_diff=abs(self.column-another_queen.column) #Calculates the absolute difference of column values of queens
            return (self.row==another_queen.row) or (self.column==another_queen.column) or (row_diff==column_diff)
