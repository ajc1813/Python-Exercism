#Acronym is formed by joining starting letters in upper case of the first word and words following delimiter(i.e. space, underscore and hyphen) 
#An empty string is first created 
#The underscore and hyphen symbols are replced by spaces using the replace() function. The string is then parsed using the split() function with space as delimiter which gives a list
#The list contains empty characters corresponding to the replaced symbols and words in the string.The empty elements are removed and a new list is formed
#Now iteration is done over the elements in the list. The first letter of each element in the list is obtined and converted to upper case and then added to the empty string

def abbreviate(words):
    acronym="" #Creates an empty string
    words_list=words.replace("-"," ").replace("_"," ").split(" ") #Replaces the the symbols hyphen and underscore in the string with space and then parses the string
    new_list = [x for x in words_list if x != ''] #Removes the empty elements from the list
    for element in new_list: #Iterates over the elementsin the list
        acronym+=element[0].upper() #Adds the starting letter of element to the empty string after converting to upper case
    return acronym 
