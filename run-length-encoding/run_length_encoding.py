#def decode(string):
    #pass
#def encode(string):
    #pass

from itertools import groupby
import re
#RLE decoding is as follows
#A list containing the numbers in the string is obtained first using list(), map() and findall() functions. For example the string '12WB12W3B24WB' gives ['12','12','3','24']
#Next the length of the list is checked
#If the length is zero, it means that the string does not have any numbers which indiactes that the string is either empty or does not have any repeated words. In this case the string is printed as such
#If length is non-zero, it means that the string has numbers. In this case first an empty string is intialized for the decoded string. Then the string is converted into a list in which each element corresponds to successive numbers or letters in the string using split fucntions. For example the string '12WB12W3B24WB' gives ['12','WB','12','W','3','B','24','WB']. Next iteration is done over one less than the length of the list(Reason for using one less length will be discussed later). The element at each index is checked whether digit or not. If an element is a digit, then the following element is considered which is a letter or group of letters. If next element i.e. (i+1)th element is a single letter, then it is repeatedly added to the string for decoded string as per number in the ith element. If the next element i.e. (i+1)th element has more than one letter, then its first letter is repeatedly added as per number in the ith element and remaining letters are added once to the string for decoded string
def decode(string):
    number_list=list(map(int, re.findall('\d+', string))) #Converts the string into a list in which each element corresponds to successive numbers or letters in the string
    if len(number_list)==0: #Checks the length of the list of numbers in the string
        return string 
    else:
        decoded_string="" #Intializes an empty string for the decoded string
        string_list = re.split('(\d+)', string) #Converts the string into a list in which each element corresponds to successive numbers or letters
        for i in range(len(string_list)-1): #Iterates over one less than length of the list
            if string_list[i].isdigit(): #Checks whether the element at the index is digit or not
                num=int(string_list[i]) #Obtains the number of repetitions
                if len(string_list[i+1])==1: #Checks whether the length of the next element is one
                    letter=string_list[i+1] #Obtains the letter to be repeatedly added
                    for x in range(num): #Iterates over the length of the next element
                        decoded_string+=letter #Adds the letter to the string for decoded string
                elif len(string_list[i+1])==2: #Checks whether the length of the next element is two
                    letter=string_list[i+1][0] #Obtains the letter to be repeatedly added
                    for x in range(num): #Iterates over the length of the next element
                        decoded_string+=letter #Adds the letter to the string for decoded string
                    decoded_string+=string_list[i+1][1] #Adds the remaining letters to the string for decoded string
                else:
                    letter=string_list[i+1][0] #Obtains the letter to be repeatedly added
                    for x in range(num): #Iterates over the length of the next element
                        decoded_string+=letter #Adds the letter to the string for decoded string
                    decoded_string+=string_list[i+1][1]+ string_list[i+1][2] #Adds the remaining letters to the string for decoded string               
        return decoded_string

#RLE encoding is as follows
#An empty string is intialized for the encoded string   
#The string is then converted to a list in which each element corresponds to group of consecutive data elements. For example, the string 'AABBBCCCC' gives ['AA','BBB','CCCC']
#Next iteration is done ob=ver the length of the list
#The length of each element is checked. If length is one, it means that letter is not repeated otherwise the letter is repeated. So if a letter is repeated, then the no:of repeatitions and the letter is added to the string for the ncoded string. If the letter is not repeated, only the letter is added to the string for encoded string
def encode(string):
    encoded_string="" #Intializes an empty string for the encoded string
    string_list = ["".join(group) for ele, group in groupby(string)] #Converts the string to a list in which each element corresponds to group of consecutive data elements
    for element in string_list: #Iterates over the length of the list
        l=len(element) #Checks the length of the element
        letter=element[0] #Obtains the letter to tbe added
        if l==1: #Checks whether the letter is repeated
            encoded_string+=letter #Adds the letter to the string for encoded string
        else:
            encoded_string+=str(l)+letter #Adds the no:of repeatitions of the letter and letter to the string for encoded string
    return encoded_string