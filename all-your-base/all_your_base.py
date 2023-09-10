#def rebase(input_base, digits, output_base):
    #pass

#As seen from the test data, the input number 'digits' is a list rather than a number
#The various exceptions are raised first:- if either input base or output base is less than 2, if list elements are negative or greater than the input base
#If the list contains only zeros or list is empty, then [0] is returned. To check whether list contains only zeros, sum() function is used which calculates the sum of elements of the list. If sum is zero, then the list contains only zeros as elements
#To convert to base 10, multiply each digit in the number with its place value. Since LCD is in left side but array begins from right, the list representing the number is first reversed. From the test data, it si seen that the number is represented as a list of integers. So the number is converted to list and is returned
#To convert a decimal number to another base, integer division is perfomed on the decimal number using the new base till the number becomes zero. the remainder obtained during each division is added to the first position of a list(From the test data we can see that output is given as a list). For this an empty list is initalized. Since the input number is given as a list of integers, it is first made into an integer using map() and join() functions and then conversion is done
#If neither input base and output base is 10, the number is first converted to base 10 and then converted to the required base
def rebase(input_base, digits, output_base, decimal = 0):
    if input_base < 2: #Checks whether the input base is less than 2
        raise ValueError("input base must be >= 2") #Raises the exception
    if output_base < 2: #Checks whether the output base is less than 2
        raise ValueError("output base must be >= 2") #Raises the exception
    if sum(1 for digit in digits if digit < 0) != 0: #Checks whether the list contains negative elements by taking count of negative elements
        raise ValueError("all digits must satisfy 0 <= d < input base") #Raises the exception
    if sum(1 for digit in digits if digit >= input_base) != 0: #Checks whether the list contains an element greater than or equal to the input base by taking count of such elements
        raise ValueError("all digits must satisfy 0 <= d < input base") #Raises the exception
    if sum(digits) == 0 or len(digits) == 0: #Checks whether the input number is empty or contains only zeros
        return [0] #Returns [0]
    if output_base == 10: #Checks whether the required base is 10
        digits.reverse() #Reverses the list representing the input
        for i in range(len(digits)):
            decimal += digits[i]*pow(input_base,i) #Calculates the decimal number
        return list(map(int, str(decimal))) #Returns the decimal number as a lsit of integers
    if input_base == 10: #Checks whether a decimal number is converted
        new = [] #Initializes an empty list for the rebased number
        num = int("".join(map(str, digits))) #Converts the list of integers into a number
        while num != 0: #Checks whether the number is zero
            new.insert(0, int(num)%output_base) #Adds the remainder of the integer division to the first position of the list representing the output
            num = num//output_base #Performs integer division on the number
        return new #Returns the numbe after conversion
    if input_base != 10 and output_base != 10: #Checks whether the bases are not equal to 10
        new = [] #Initializes an empty list for the rebased number
        digits.reverse() #Reverses the list representing the input
        for i in range(len(digits)):
            decimal += digits[i]*pow(input_base,i) #Calculates the decimal number corresponding to the input
        while decimal != 0: #Checks whether the number is zero
            new.insert(0, int(decimal)%output_base) #Adds the remainder of the integer division to the first position of the list representing the output
            decimal = decimal//output_base #Performs integer division on the number
        return new #Returns the numbe after conversion