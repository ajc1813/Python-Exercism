#def roman(number):
    #pass

#Four dictionaries are created for ones, tens, hundreds and thousands position. The key-value pair in each dictionary represent a number's position and ocrresponding letter
#The given number is convrted into a list using list() function. Since list() function takes only string, the number is first converted into a string using str() function and then into a list
#Each element in the list obtained form the number is enclosed in quotes which means that they are of string type. But the list elements are used as key values to fetch values from the dictionaries and in dictionaries, the keys are integer type. So when string value is used as key fetch value from the dictionaries, KeyError will occur. To avoid this the lements are converted into integer type
#The list now contains, the digits of the number starting from thousands position to one's position. The number of digits in the number may vary from 1 to 4 and alteast one digit is always present which is the one's position. So the list isreversed so that the digit at the one's postion appears in the beginning of the list
#Next each digit in the list and its index is obtained using the enumerate() function. According to the index, an appropriate dictionary is selected and value of the key corresponding to the digit is obtained from the dictionary and added to the string for roman numeral
def roman(number):
    ones_dict={0:'',
               1:'I',
               2:'II',
               3:'III',
               4:'IV',
               5:'V',
               6:'VI',
               7:'VII',
               8:'VIII',
               9:'IX',
               10:'X'} #Creates a dictionary for one's position
    tens_dict={0:'',
               1:'X',
               2:'XX',
               3:'XXX',
               4:'XL',
               5:'L',
               6:'LX',
               7:'LXX',
               8:'LXXX',
               9:'XC'} #Creates a dictionary for ten's position
    hundreds_dict={0:'',
                   1:'C',
                   2:'CC',
                   3:'CCC',
                   4:'CD',
                   5:'D',
                   6:'DC',
                   7:'DCC',
                   8:'DCCC',
                   9:'CM'} #Creates a dictionary for hundred's position
    thousands_dict={1:'M',
                    2:'MM',
                    3:'MMM'} #Creates a dictionary thousand's position
    roman_numeral="" #Creates an empty string for the roamn numeral 
    number_list=list(str(number)) #Converts the number into a list
    number_list=[int(digit) for digit in number_list] #Converts the list of strings into a list of integers
    number_list.reverse() #Reverses the list
    for index,digit in enumerate(number_list):
        if index==0: #Checks whether the index of the digit is 0
            roman_numeral+=ones_dict[digit] #Adds the value of the key corresponding to the digit from the one's dictionary to the string for roman numeral
        elif index==1: #Checks whether the index of the digit is 1
            roman_numeral=tens_dict[digit]+roman_numeral #Adds the value of the key corresponding to the digit from the ten's dictionary to the string for roman numeral
        elif index==2: #Checks whether the index of the digit is 2
            roman_numeral=hundreds_dict[digit]+roman_numeral #Adds the value of the key corresponding to the digit from the hundred's dictionary to the string for roman numeral
        elif index==3: #Checks whether the index of the digit is 3
            roman_numeral=thousands_dict[digit]+roman_numeral #Adds the value of the key corresponding to the digit from the thousand's dictionary to the string for roman numeral
        else:
            roman_numeral+=''
    return roman_numeral