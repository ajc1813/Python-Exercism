#def say(number):
    #pass

#Dictionaries for letters corresponding to ones place, tens place, numbers between 11 and 19, higher places are defined. A function to define word corresponding to a three digit number is then created. Next a function to obtain the word corresponding to a number of any length is defined
import textwrap #Imports the textwrap module
ones_dict={0:'zero',
           1:'one',
           2:'two',
           3:'three',
           4:'four',
           5:'five',
           6:'six',
           7:'seven',
           8:'eigth',
           9:'nine'} #Creates a dictionary in which each key-value pair represent a number and its corresponding word in ones place
new_dict={11:'eleven',
          12:'twelve',
          13:'thirteen',
          14:'fourteen',
          15:'fifteen',
          16:'sixteen',
          17:'seventeen',
          18:'eighteen',
          19:'nineteen'} #Creates a dictionary in which each key-value pair represent a number between 11 and 19 and its corresponding word
tens_dict={2:'twenty',
           3:'thirty',
           4:'forty',
           5:'fifty',
           6:'sixty',
           7:'seventy',
           8:'eighty',
           9:'ninety'} #Creates a dictionary in which each key-value pair represent a number and its corresponding word in tens place
high_dict={1:'thousand',
           2:'million',
           3:'billion'} #Creates a dictionary in which each key-value pair represent a number and its corresponding position

#The function for defining the word corresponding to a three digit number is define below.
#A empty string is initialized for the word corresponding to the three digit number
#The three digit number is converted into a list of digits. The digits in the list will be enclosed in quotes which means they are of string type. This is ok if the key in the dictionaries are also enclosed in quotes or they are of string type otherwise KeyError will occur. in order to convert the list elements type to integer, int() is used with each digit
#Then another list which indicates the indices where non-zero elements are present in the list obtained from the number
#The length of the index list is checked
#If length is zero, it means that all digits in the number is zero and space is added to the string for the word. Later the this function is used to obtain word corresponding to a number of any length. Then the space will appear. So the space is removed using strip() fucntion
#If length is one, it means that only one digit in the number is non-zero. This could be index position 0, 1 or 2. According to the index position, corresponding dictionary is choosen and word corresponding to the digit is elected from the dictionary
#If length is two, it means that two digits in the number is non-zero. There are three posibilities in this case as follows. The non-zero elements could be in first and second position of the list of digits or could be in first and third position of the list of digits or could be in third and second position of the list of digits. In the first case, the non-zero elements are in ones place and tens place. So corresponding words are obtained from the dictionaries corresponding to ones place and tens place. In the thirs case, the non-zero elements are in tens place and hundreds place. So dictionary corresponding to tens place is used and word 'hundred' is used to indicate element in hundreds place
#If length is three, it means that all digits in the number are non-zero. In this case, the word corresponding to the digit in ones place is obtained from the dictionary corresponding to ones place and is added to the string for word. Then the word corresponding to the digit in tens place is obtained from the dictionary corresponding to tens place and is added to the string for word. Finally the word corresponding to the digit in hundreds place is obtained from the dictionary corresponding to ones place and is added to the string for word alond with the word 'hundred'
def word(number):
    num_word="" #Creates an empty string fot the word corresponding to the number
    digit_list=[int(digit) for digit in number] #Converts the number into a list of digits
    digit_index_list=[digit_index for digit_index,digit in enumerate(digit_list) if digit!=0] #Creates a list indicating indices where non-zero elements are present in the list from the number
    if len(digit_index_list)==0: #Checks whether the length of the list of indices of non-zero elements is zero
        num_word+="" #Adds space to the string for the word 
    elif len(digit_index_list)==1: #Checks whether the length of the list of indices of non-zero elements is one
        index=digit_index_list[0] #Finds the index of the non-zero element
        digit=digit_list[index] #Finds the non-zero element in the list
        if index==0: #Checks whether the non-zero element is at index 0
            num_word+=ones_dict[digit] #Adds the word corresponding to the digit from the dictionary for ones place
        elif index==1: #Checks whether the non-zero element is at index 1
            num_word+=tens_dict[digit] #Adds the word corresponding to the digit from the dictionary for tens place
        elif index==2: #Checks whether the non-zero element is at index 2
            num_word+=ones_dict[digit]+" "+"hundred" #Adds the word corresponding to the digit from the dictionary for ones place and the word 'hundred' after a space
    elif len(digit_index_list)==2: #Checks whether the length of the list of indices of non-zero elements is two
        if digit_list[0]!=0 and digit_list[1]!=0: #Checks whether the non-zero elements are in the index 0 and 1
            for index in digit_index_list: #Itrerates over the list of index of non-zero elements
                digit=digit_list[index] #Obtains the element at the index position
                if index==0: #Checks whether the index is zero
                    num_word+=ones_dict[digit] #Adds the word corresponding to digit in ones place to the string for word
                elif index==1: #Checks whether the index is one
                    num_word=tens_dict[digit]+'-'+num_word #Adds the word corresponding to digit in tens place to the string for word
        elif digit_list[1]!=0 and digit_list[2]!=0: #Checks whether the non-zero elements are in the index 2 and 1
            for index in digit_index_list: #Itrerates over the list of index of non-zero elements
                digit=digit_list[index] #Obtains the element at the index position
                if index==1: #Checks whether the index is one
                    num_word+=tens_dict[digit] #Adds the word corresponding to digit in tens place to the string for word
                elif index==2:
                    num_word=ones_dict[digit]+" "+"hundred"+" "+num_word  #Adds the word corresponding to digit in hundreds place and the word 'hundred' to the string for word          
    elif len(digit_index_list)==3: #Checks whether the length of the list of indices of non-zero elements is three
        for index in digit_index_list: #Itrerates over the list of index of non-zero elements
            digit=digit_list[index] #Obtains the element at the index position
            if index==0: #Checks whether the index is zero
                num_word+=ones_dict[digit] #Adds the word corresponding to digit in ones place to the string for word
            elif index==1: #Checks whether the index is one
                num_word=tens_dict[digit]+'-'+num_word #Adds the word corresponding to digit in tens place to the string for word
            else: 
                num_word=ones_dict[digit]+" "+"hundred"+" "+num_word #Adds the word corresponding to digit in hundreds place to the string for word along with the word 'hundred'
    else:
        return None
    return num_word 

#The function for defining the word corresponding to a given digit number is define below
#First check whether number is negative or greater than 999999999999
#If yes raise ValueError. Then number is checked for zero, between 11 and 19, 1000000 and 1000000000
#If no, the number is to grouped to three elements. But this is done from right to left. But it should be done from left of the number to the right. So number is first reversed
#The reversed number is converted into a list obtained by grouping three elements of the reversed number from right using textwrap() function
#Next a list indicating indices of elements of above list is obtained. Each element contains three digits. So index 1,2,3 represent thousand, million and billion respectively
#Iteration is done over the list obtained from the number
#Since each element contain three digits, the word corresponding to it is obtained using the word() fucntion. Now appropriate words is selced from the dictionary for higher position and the word corresponding to number is obtained
#Now in the word 
def say(number):
    if number<0 or number>999999999999: #Checks whether number is negative or greater than 999999999999
        raise ValueError("input out of range") #Raises ValueError
    elif number==0: #Checks whether number is zero
        return 'zero'
    elif number>=11 and number<=19: #Checks whether number is between 11 and 19
        return new_dict[number] 
    elif number==1000000: #Checks whether number is 1000000
        return "one million"
    elif number==1000000000: #Checks whether number is 1000000000
        return "one billion"
    else:
        reversed_number = '' #Initializes an empty dtring for the reversed string
        number_word='' #Initializes an empty string for the word corresponding the number
        while number > 0: #Checks whether the number is greater than zero
            last_digit = number % 10 #Obtains the last digit of the number
            reversed_number = reversed_number + str(last_digit) #Adds the last digit to the string for reversed string
            number = number // 10 #Performs division on the number
        number_list=textwrap.wrap(str(reversed_number), 3) #Converts the reversed number into a list by grouping three numbers of the number
        index_list=[index for index,element in enumerate(number_list)] #obtains the list of indices of elements of the list obtained from the number
        for index,element in enumerate(number_list): #iterates over the list obtined from the number
            element_word=word(element) #obtain the word corresponding to element using word() function
            if index==0: #Checks whether index of the element is zero
                number_word+=element_word #Adds the word corresponding to the element to the string for word
            else:
                number_word=element_word+' '+high_dict[index]+" "+number_word #Adds the word corresponding to the element to the string for word along with appropriate positions    
                number_word=number_word.rstrip(" ") #removes space added in the word function when length of the index list is zero
        return number_word       