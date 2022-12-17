#According to test data, a valid ISBN should satisfy the following conditions
#Length should be 10[which can be done using len() function]
#The first 9 digits should not contain any letters[which can be checked using the isdigit() function]
#The last digit(Check digit) should be either alphabet 'X'[which can be done by first checking whether the check digit is an alphabet using isaplha() function and if true, then check wthether the alphabet is X] or a number 
#If the check digit is alphabet 'X', then its value should not be 0. This is checked in the following way. An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero. in other words for an ISBN 10 number to be valid we multiply the first digit by 10, the second by 9, the third by 8 etc. down to the 10th digit by 1 and if the result is divisible by 11 then the code is valid. If check digit is zero, then sum of first 9 digits(i.e. digits other than check digit) multiplied by their position itself will be a multiple of 11. Otherwise check digit will be number in between 0 and 9 which when added to the above sum gives a multiple of 11
#if all above conditions are satisfied, then sum of the digits multiplied by their position modulo 11 should be zero

def is_valid(isbn):
    isbn=isbn.replace("-","") #Removes dash symbol 
    if len(str(isbn))!=10 : #Checks whether the length is 10
        return False
    else:
        if isbn[:-1].isdigit(): #Checks whether the first 9 digits contains any alphabets
            if isbn[-1].isalpha(): #Checks whether the check digit is an alphabet
                if isbn[-1]=="X": #Checks whether the check digit is the alphabet 'X'
                    sum=0 #initializes a variable 'sum'
                    for i in range(9): #Calculates the sum of the first nine digits multiplied by their position. Here range given is one less than length of ISBN since check digit is not needed
                        sum = sum + int(isbn[i]) * (10 - i) 
                    remainder=sum%11 #Calculates the remainder when divided by 11
                    return remainder!=0 #Checks whether the remainder is zero
                else:
                    return False
            else:
                sum=0
                for i in range(10): #Calculates the sum of the digits multiplied by their position
                    sum = sum + int(isbn[i]) * (10 - i) 
                return sum % 11 == 0 #Checks whether the remainder is zero when divided by 11
        else:
            return False
        
            
