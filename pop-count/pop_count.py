#def egg_count(display_value):
    #pass

#The display_value is converted into binary value using the bin() function. In the binary value obtained starts with "0b" which is removed using the replace() function. the number of ones in the binary value is then counted
def egg_count(display_value):
    bynary = bin(display_value).replace("0b", "") #Converts the display_value into binary value
    count = sum([1 for i in bynary if i == "1"]) #Counts the number of ones
    return count