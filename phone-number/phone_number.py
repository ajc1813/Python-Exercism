#class PhoneNumber:
    #def __init__(self, number):
        #pass

#In the tests it is given 'number = PhoneNumber("(223) 456-7890").number' and 'PhoneNumber("(223) 456-7890").area_code'. 'PhoneNumber("(223) 456-7890")' is an object of the class "PhoneNumber". Then 'PhoneNumber("(223) 456-7890").number' and 'PhoneNumber("(223) 456-7890").area_code' indicates that the class PhoneNumber has two instance properties namely number and area_code. 'number = PhoneNumber("(223) 456-7890").number' indicates that number is the value of the instance property 'number' of the class 'PhoneNumber'
#Also in the tests it is given 'number.pretty()'. number, which is an object, followed by the word 'pretty' which is followed by '()' indicates that 'pretty' is an instance. Thus there is an instance method 'pretty()' associated with the class
#Solution is as follows
#The instances properties of the class 'PhoneNumber':-number and area_code are first created. number is created by removing the symbols(".","-","+","(",")") and space from the number parameter. area_code is obtained by slicing out the first three digits of the instance property 'number'
#Next length of the instance property is checked. If length is less than 10 or greater than 11 then ValueErrors are raised. If length is 11, then starting digit of the instance property 'number' is checked. If it is zero, then Valueerror is raised and if it is one, the one is removed
#The starting digit of the area code and exchange codes is then evaluated. if it is either 0 or i, then ValueError is raised. In the test, result are given in quotes which means that the result is a string. So while checking for starting digit of area and exchange codes, they are given in quotes
#Next instance property 'number' is checked for alphanumeric characters i.e. a-z and 1-9. if yes, then it is checked for digits. If letters are present, ValueError is raised

class PhoneNumber:
    def __init__(self, number):
        self.number=number.replace(".","").replace("-","").replace("(","").replace(")","").replace(" ","").replace("+","") #Creates the instance property 'number'
        self.area_code=self.number[0:3] #Creates the instance property 'area_code'
        
        if len(self.number)<10: #Checks whether length of the instance property 'number' is less than 10
            raise ValueError("incorrect number of digits") #Raises the ValueError
        elif len(self.number)==11: #Checks whether length of the instance property 'number' is equal to 11
            if self.number[0]!="1": #Checks whether the starting digit is a digit other than 1
                raise ValueError("11 digits must start with 1") #Raises the ValueError
            if self.number[0]=="1": #Checks whether the starting digit 1
                self.number=self.number[1:] #Removes 1
        elif len(self.number)>11: #Checks whether length of the instance property 'number' is greater than 11
            raise ValueError("more than 11 digits") #Raises the ValueError
        else:
            None
            
        if self.number.isalnum(): #Checks the instance property 'number' contains only alphanumeric characters
            if not self.number.isdigit(): #Checks the instance property 'number' contains letters
                raise ValueError("letters not permitted") #Raises the ValueError
        else:
            raise ValueError("punctuations not permitted") #Raises the ValueError
            
        if self.number[0]=="0": #Checks whether the area code starts with 0
            raise ValueError("area code cannot start with zero") #Raises the ValueError
        if self.number[0]=="1": #Checks whether the area code starts with 1
            raise ValueError("area code cannot start with one") #Raises the ValueError
        if self.number[3]=="0": #Checks whether the exchange code starts with 0
            raise ValueError("exchange code cannot start with zero") #Raises the ValueError
        if self.number[3]=="1": #Checks whether the exchange code starts with 1
            raise ValueError("exchange code cannot start with one") #Raises the ValueError
        
    def pretty(self): #Creates th instance method 'pretty'
        return "("+self.number[0:3]+")"+"-"+self.number[3:6]+"-"+self.number[6:]
            
        