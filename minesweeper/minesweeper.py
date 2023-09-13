#def annotate(minefield):
    # Function body starts here
    #pass

#As per the test data, ValueError should be raised if the elements have different length. For this a list of lengths of the elements are formed which is then converted to a set. Since set removes duplications, set will have only one element if all the elemenet lengths are equal else it will will have more than one element
#If a location has space, then check whether the location is in the uppermost or lowermost rows. 
#If it is not in the uppermost row, check whether the position located vertically above is "*". If "*" is present, increment the count. Next check whther the location is in the leftmost or rightmost columns. if it is not in the leftmost column, then check whether the top left diagonal position is "*". If "*" is present, increment the count. if it is not in the rightmost column, then check whether the top right diagonal position is "*". If "*" is present, increment the count.
#If it is not in the lowermost row, check whether the position located vertically below is "*". If "*" is present, increment the count. Next check whther the location is in the leftmost or rightmost columns. if it is not in the leftmost column, then check whether the bottom left diagonal position is "*". If "*" is present, increment the count. if it is not in the rightmost column, then check whether the bottom right diagonal position is "*". If "*" is present, increment the count

def annotate(minefield):
    if not minefield:
        return []
        
    if len(set([len(e) for e in minefield])) != 1: #Checks whether length of the set obtained from list of element lengths is not one
        raise ValueError("The board is invalid with current input.") #Raises ValueError

    for i in range(len(minefield)): #Iterates across the rows
        for j in range(len(minefield[0])): #Iterates across the columns
            if minefield[i][j] not in [' ', '*']: #Checks whether a position contains character other than '*' or ""
                raise ValueError("The board is invalid with current input.") #Raises ValueError 
            if minefield[i][j] == ' ': #Checks whether a position has blank space 
                count = 0 #Initializes a variable for count
                if i != 0: #Checks whether the row is not the uppermost row
                    if minefield[i - 1][j] == '*': #Checks whether the position located vertically above has "*"
                        count += 1 #Increments the count
                    if j != 0 and minefield[i - 1][j - 1] == '*': #Checks whether the column is not the leftmost column and the top left diagonal position has "*"
                        count += 1 #Increments the count
                    if j != len(minefield[0]) - 1 and minefield[i - 1][j + 1] == '*': #Checks whether the column is not the rightmost column and the top right diagonal position has "*"
                        count += 1 #Increments the count
                if i != len(minefield) - 1: #Checks whether the row is not the lowermost row
                    if minefield[i + 1][j] == '*': #Checks whether the position located vertically below has "*"
                        count += 1 #Increments the count
                    if j != 0 and minefield[i + 1][j - 1] == '*': #Checks whether the column is not the leftmost column and the bottom left diagonal position has "*"
                        count += 1 #Increments the count
                    if j != len(minefield[0]) - 1 and minefield[i + 1][j + 1] == '*': #Checks whether the column is not the rightmost column and the bottom right diagonal position has "*"
                        count += 1 #Increments the count
                if j != 0 and minefield[i][j - 1] == '*': #Checks whether the column is not the leftmost column and the position located horizontally left is "*"
                    count += 1 #Increments the count
                if j != len(minefield[0]) - 1 and minefield[i][j + 1] == '*': #Checks whether the column is not the rightmost column and the position located horizontally right is "*"
                    count += 1 #Increments the count
                if count:
                    minefield[i] = f"{minefield[i][:j]}{count}{minefield[i][j + 1:]}"
    return minefield