#def combinations(target, size, exclude):
    #pass     

#Since killer sudokku uses numbers 1 to 9, a list containing numbers 1 to 9 is first created
#A list of all sublists of this list whose length is equal to given size and sum is equal to given target are created
#The sublists in the list are sorted in ascending order of the first element as required in test data
#If no restricted combination are present the list is returned
#Else a list of all sublists that contains elements of exclude list is created and difference between the lists of all sublists and lists of sublists containing restrcited elements is calculated which gives the rquired output
def combinations(target, size, exclude):
    sublists_list = []
    restricted_list = []
    uniqueList = []
    duplicateList = []
    killer_sudokku = []
    numbers = [num for num in list(range(1,10))] #Creates a list of numbers 1 to 9
    sublists_list = [x for x in subsets(numbers) if len(x)==size and sum(x)==target] #Creates a list of required sublists
    sublists_list.sort(key = lambda x: x[0]) #Sorts the list of sublists
    if len(exclude) == 0: #Checks whether any restricted elemnets are present
        killer_sudokku = sublists_list
    else:
        for num in exclude: #Iterates across the elements to be excluded
            for sublyst in sublists_list: #Iterates across the sublists
                if num in sublyst: #Checks whether the excluded element is present in the sublists
                    restricted_list.append(sublyst) #Appends the sublist to a list
        for element in sublists_list: #Iterates across the sublists
            if element not in restricted_list: #Checks whether the sublist is in the list of restricted sublists
                killer_sudokku.append(element) #Appends the sublist to the output
    return killer_sudokku #Returns the killer sudokku output

#Function for creating all possible sublists of a given list
def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]