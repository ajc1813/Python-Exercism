#def transpose(lines):
    #pass

#First the input text is checked for multiple rows. If multiple rows are present, the newline symbol will be present in the input text
#If multiple rows are not present, the text may be either empty or has only one row. If the input text is empty, it is returned as such else newline symbol is added after each character in the input text. This causes a newline symbol after the last character which is not required. So the last newline character is removed which gives the transpose of the input text
#If multiple rows are present, the text is converted into a list using split() function with newline character as delimiter. Each element of the list corresponds to text between two newline characters in the input text. Next the length list elements should be same(Reason will be discussed later). If they are different, the lengths of all the list elements are made equal. For this the length of the list element with maximum length is found and an empty list is initialized for the list in which all elements have equal length. Now iteartion is done over the elements of the list obtained from the input text. If element length is less than the maximum element length, then "@" symbol is padded at the end of the element till its length becomes the maximum length(Reaso for using "@" symbol will be discussed later). Thus a list in which all elements have equal length is obtained. Now each row of the transpose is calculated. For this corresponding elements of the list elements are done(If this operation is done in a list with varying elements elengths, then IndexError will occur. To avoid this the lengths of list elemnts were made equal). For performing the sum operation an empty string is initialized for the transpose of the input text. Iteration is done over the range of maximum element length. An empty string is intialialized for row of the transpose. Iteration is done over the elements of the list with equal element lengths and the corresponding element characters are concatenated. After each iteration a string is obtained. This may contains characters, space and @ symbols. But as per tests, if the space is due to padding, then it should be removed else it can retained. For example '.@' means there is a space after dot which is due to the padding and it should not present in the output. So @ symbols after characters are removd using rstrip() function. Now there may be @ symbol before characters. Since space before characters should be retained, they are repaced with space using replace() fnction(If padding was done using space instead of @ symbol, this differential tretament of @ symbols before and after characters would not have been possible. If space was used and replace function was used to remove space after characters, then space before characters also will be removed). This a row in the transpose is obtained. Now each row row is added to the string for transpose along with a newline symbol. In this process, a newline character will be added after the last row also which is required. So the last newline character is removed
def transpose(lines):
    if "\n" not in lines: #Checks whether newline symbol is present in the text
        if len(lines)==0: #Checks whether the input text is empty
            return lines #Returns the input text
        else:
            single_column="" #Initializes an empty string for the the transpose of the single row which is a single column
            for i in range(len(lines)): #Iterates over the length of the input text
                single_column+=lines[i]+"\n" #Adds the character and the newline symbol to the string for the transpose
            transpose=single_column[:-1] #Removes the last character from the string which is a newline character
            return transpose
    else:
        lines_list=lines.split("\n") #Splits the input text
        max_len=len(max(lines_list, key=len)) #Calculates the highest element length
        equi_len_list=[] #Initializes an empty list for the list having eqaul element lengths
        for element in lines_list: #Iterates over the elements of the list obtained from the input text
            if len(element)<max_len: #Checks whether the length of the element is less than the maximum element length of the list
                element=element.ljust(max_len,"@") #Adds "@" symbols 
                equi_len_list+=[element] #Adds the element tot he list for equal length elements
            else:
                equi_len_list+=[element] #Adds the element tot he list for equal length elements
                
        transpose="" #Initializes an empty string for the transpose of the input text
        for i in range(max_len): #Iterates over the range of maximum element length
            transpose_row="" #Initializes an empty string for the row of the transpose
            for element in equi_len_list: #Iterates over the elements of the list with equal element length
                transpose_row+=element[i] #Concatenates the corresponding element characters
            transpose_row=transpose_row.rstrip("@").replace("@"," ") #Removes the @ symbols after the characters and replaces the @ symbol before characters with space
            transpose+=transpose_row+"\n" #Adds the row to the string for the transpose with a newline character
        transpose=transpose[:-1] #Removes the last character from the string which is a newline character
        return transpose