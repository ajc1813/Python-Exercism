#The steps for obtaining the Atbash Cipher is as follows. The space and symbols(coma, punctuation mark) are removed from the plain text which obtains a string with only one word which is converted to lower case. The plain text is arranged into group of five conecutive letters in the plain text. Each alphabet in the group is replaced by a reciprocal alphabet/mirrored alphanet(alphabet whose index position in the list of alphabets a-z in descending order is same as that of the list of alphabets a-z in the ascending order) and numbers are kept unchanged
#The steps for decoding is as follows. The space ais removed from the cipher text which obtains a string with only one word. Each alphabet in the string is replaced by a reciprocal alphabet/mirrored alphanet(alphabet whose index position in the list of alphabets a-z in ascending order is same as that of the list of alphabets a-z in the descending order) and numbers are kept unchanged
#For solving the exercise, a list containing alphabets a to z in ascending order and list containing the alphabets a to z in descending order is defined
#For encoding, an empty list and an empty string is obtained. The plain text is converted to lower case using lower() function and space, coma, punctuation marks are removed from it using replace() function. A list is obtained from the plain text, using the wrap() function, in which each element is formed by five consecutive letters in the plain text. Next iteration is done over the elements of the list and then iteration is done over the letters in each element in the list. If the letter is alphabet, then it is replaced by its reverse alphabet and if the letter is a number, it is kept unchanged. The cipher corresponding to each element is added as element of the empty list. Thus after after iteration a list is obtained in which each element is a cipher corresponding to the element in the list obtained from the plain text. This list is converted into a string using join() function with space between elements of the list
#For decoding, an empty string isdefined. The space is removed from the cipher text using the replace() function. Next iteration is done over the letters in the cipher text. If the letter is alphabet, then it is replaced by its reverse alphabet and if the letter is a number, it is kept unchanged.

import textwrap #Imports the textwrap module 
alphabets=list('abcdefghijklmnopqrstuvwxyz') #Creates a list containing aplhabets in ascending order
cipher_alphabets=alphabets[::-1] #Creates a list containing aplhabets in descending order

def encode(plain_text):
    cipher_list=[] #Creates an empty list
    plain_text=plain_text.lower().replace(" ","").replace(",","").replace(".","") #Converts the plain text into lower case and removes space and symbols from it
    lst=textwrap.wrap(plain_text, 5) #Converts the plain text into a list in which each element is formed by five consecutive letters in the plain text
    for word in lst: #Iterates over the elements of the list
        word_cipher="" #Creates an empty string
        for letter in word: #Iterates over the letters of the word
            if letter.isalpha(): #Checks whether the letter is alphabet or not
                index=alphabets.index(letter) #Obtains the index of the letter in the list containg alphabets in ascending order
                word_cipher+=cipher_alphabets[index] #Obtains the reverse alphabet and adds it to the empty string
            else:
                word_cipher+=letter #Adds the letter as such to the empty string
        cipher_list.append(word_cipher) #Adds the cipher corresponding to element in the list to the empty list
    return " ".join(cipher_list) #Converts the list into a string which is the cipher text
            
def decode(ciphered_text):
    plain_text="" #Creates an empty string
    ciphered_text=ciphered_text.replace(" ","") #Removes space from cipher text
    for letter in ciphered_text: #Iterates over the letters in the cipher text
        if letter.isalpha(): #Checks whether the letter is alphabet or not
            index=alphabets.index(letter) #Obtains the index of the letter in the list containg alphabets in descending order
            plain_text+=cipher_alphabets[index] #Obtains the reverse alphabet and adds it to the empty string
        else:
            plain_text+=letter #Adds the letter as such to the empty string
    return plain_text #Returns the plain text