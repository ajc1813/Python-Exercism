#def cipher_text(plain_text):
    #pass

#The plain text is first normaized by removing the symbols
#The length of the normalized text is then checked
#If the length is zero, the normalized text is returned
#Else the rows and columns are determined. For this the square root of the length of the normalized text is calculated. If it is a perfect square, then the square root value is taken as the number of rows and number of columns. Else the integer part of the sqaure root is taken as the number of rows and number of columns is obtained by adding one to the value of the number of rows. Now the normalized text is converted into a list in which each element has a length equal to the number of columns. The length of the elements in the list should have equal length which is equal to the number of columns(Reason will be stated later). For this an empty list is initialized. If length of an element in the list obtained from the normalized text is less than the number of columns, then padding is done using the symbol "@"(Reason for using @ symbol will be discussed later). Thus the given text is converted into list whose element correspond to a row of a rectangle. Next is to form the coded message which is obtained by reading down the columns going left to right. For this characters at corresponding index positions of list elements are added which will give a row in the rectange corresponding to the coded message(If the list elements do not have equal length, then IndexError will occur during this addition. To avoid the error, the list elementys were made equi-legth).The row obtained are added up along with a space. In the end there will be extra space which is removed using rstip() function and the "@" symbol which was padded is also removed. If the space was used for padding instead of "@" symbol, then last space also will be removed while using rstrip() that is why "@" symbol was used for padding
import textwrap #Imports the textwrap module
import math #Imports the math module
def cipher_text(plain_text):
    normalized_text=plain_text.replace("-","").replace(".","").replace("@","").replace(",","").replace("%","").replace("!","").replace(" ","").lower() #Removes the symbols to obtain the normalized text
    if len(normalized_text)==0: #Checks whether the length of the normalized text is zero
        return normalized_text
    else:
        square_root=math.sqrt(len(normalized_text)) #Calculates the square root of the length of the normalized text
        if square_root.is_integer(): #Checks whether the square root is an integer
            r=int(square_root) #Assigns the sqaure root as the number of rows
            c=int(square_root) #Assigns the sqaure root as the number of columns
        else:
            r=int(square_root) #Assigns the integer part of the sqaure root as the number of rows
            c=r+1 #Calculates the number of columns
        text_list=textwrap.wrap(normalized_text, c) #Converts the normalised text into a list
        equi_len_list=[] #Initializes an empty list for list with equi-length elements
        for element in text_list: #
            if len(element)<c: #Checks whether the length of the list element is less than the no:of columns
                element=element.ljust(c,"@") #Adds @ symbol to the left end of the list element
                equi_len_list+=[element] #Adds the element to the list for list with equi-length elements
            else:
                equi_len_list+=[element] #Adds the element to the list for list with equi-length elements
        crypto_square="" #Initializes an empty string for coded message
        for i in range(c):  # Iterates over the number of columns
            crypto_square_row="" #Initializes an empty string for a row in the coded message
            for element in equi_len_list: #Iterates over the elements of the list
                crypto_square_row+=element[i] #Adds the characters at corresponding index positions of list elements
            
            crypto_square+=crypto_square_row+" " #Adds the row of the coded message to the sttring for the coded message along with a space
        crypto_square=crypto_square.rstrip().replace("@"," ") #Removes the space at the trailing end of the coded message and replaces the "@" symbol
        return crypto_square