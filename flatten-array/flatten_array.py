#Initialize an empty list. Each element in the input list is extracted. Each extracted element can be a integer, list or nested list. So check whether the extracted element is a list or an integer. If it is an integer, then add it to the empty list. If it is a list check whether it contains any nested list. If no nested list is present, add it to the empty list list 'extend' command. If nested list is present, then convert the element into a list using 'flatten' command and then add it to the empty list. Now the list ithout any nested list is ready. then the 'None' should be removed
def flatten(iterable):
    flat_array=[] #initializes the empty list
    for element in iterable: #Extracts each element in the input list
        if type(element) is list: #checks whether the extracted element is a list
            flat_array+=flatten(element)        
        else:
            flat_array.append(element) #Adds the integer element to the empty list
    while flat_array.count(None): #checks whether count of 'None' is zero in the list
        flat_array.remove(None) #Removes 'none' from the list
    return flat_array
    
        
        
