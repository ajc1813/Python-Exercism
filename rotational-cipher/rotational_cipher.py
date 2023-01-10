#Two lists are first created:-one containing all lower case alphabets and oother containing all upper case letters
#An empty string is then created
#Now iteration over characters of a string is carried out
#Each character is checked whether it is an alphabet or not
#If not an aplhabet(i.e. space or punctuation mark or number) it is unchanged as per the test cases and so it is added as it is to the empty string
#If the character is an aplhabet, then it is checked whether it is a lower case or upper case
#If the character is lower case, then to obtain the cipher it should be replaced by another element in the list of lower case letters. To determine the new character, method is as follows. At first the index of the original character in the list of lower case letters is found which is then added to the key. If the sum is less than the lenegth of the list of lower case letters(no:of lower case alphabets), then this character whose index equal to the above sum replaces the character. If sum is greater than 26 which means wrap around occurs, then new index = which beobtain the cipher, the character should be replaced by a character at a new index equal to the sum of the index of the character and the key. If the sum is less than the length of the list of lower case alphabets, then simply add the new character to the empty string. Else the new index is calculated as follows. The difference of length of list of lower case letters and index is calculated which is subtracted from the key. The charcater at this index value is the new character
#If the character is upper case, method is same as that for lowrer case, except that here list used is the list of upper case alphabets instead of list of lower case letters

def rotate(text, key):
    lower_alphabets=list('abcdefghijklmnopqrstuvwxyz') #Creates a list containing all lower case alphabets.The list can also be created by specifying all the lower case aplhabets in quotes and seperated by commas. This is the easier method
    upper_alphabets=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') #Creates a list containing all upper case alphabets.The list can also be created by specifying all the upper case aplhabets in quotes and seperated by commas. This is the easier method
    cipher="" #Creates an empty string
    for character in text: #Iterates over the characters in the string
        if character.isalpha(): #Checks whether the character is an aplhabet
            if character.islower(): #Checks whether the character is a lower case aplhabet
                index=lower_alphabets.index(character) #Obtains the index of the character from the list of lower case alphabets
                if (index+key)<=(len(lower_alphabets)-1): #Checks whether wrap around is present
                    cipher+=lower_alphabets[index+key] #Adds the new character from the list of lower case letters to the string
                else:
                    cipher+=lower_alphabets[key-(len(lower_alphabets)-index)] #Adds the new character from the list of lower case letters to the string
            else:
                index=upper_alphabets.index(character) #Obtains the index of the character from the list of upper case alphabets
                if (index+key)<=(len(upper_alphabets)-1): #Checks whether wrap around is present
                    cipher+=upper_alphabets[index+key] #Adds the new character from the list of upper case letters to the string
                else:
                    cipher+=upper_alphabets[key-(len(upper_alphabets)-index)] #Adds the new character from the list of upper case letters to the string
        else:
            cipher+=character #Adds the non-alphabet characters in the string to the empty string
    return cipher #Returns the cipher                   