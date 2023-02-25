#class Matrix:
    #def __init__(self, matrix_string):
        #pass
    #def row(self, index):
        #pass
    #def column(self, index):
        #pass

#The given string is converted into a list using split() function with newline character as delimiter
#To find the required row, element at index position one less than the given index is obtained which is a string containing numbers seperated by space(s). So this string is converted into a list using split() function with space as delimiter. Then a list of string is obtained which is then convrted to a list of integers
#To find the column, each element in the list obtained from the given string is converted into a list using split() function with space as the delimiter thereby forming a nested list. Next a list of element corresponding to position one less than the given index from all the nested lists is formed which is a list of strings. This list of string is converted to a list of integers
class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string=matrix_string.split("\n") #Converts the given string into a list
              
    def row(self, index):
        self.string_list=self.matrix_string[index-1] #Obtains the element at position (index-1) from the list obtained from the given string
        self.element=self.string_list.split(" ") #Converst the element into a list of strings
        self.raw=[int(digit) for digit in self.element] #Converts the list of string to a list of integers
        return self.raw
        
    def column(self, index):
        self.string_list=[element.split(" ") for element in self.matrix_string] #Converts each element of the list obtained from the given into a list
        self.col=[element[index-1] for element in self.string_list] #Forms a list of string using elements of the nested lists at index position one less than the given index
        self.col=[int(digit) for digit in self.col] #Converts the list of strings to list of integers
        return self.col
