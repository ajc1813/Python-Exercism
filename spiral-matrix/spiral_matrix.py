#def spiral_matrix(size):
    #pass

#A 2D matrix of zeros of the given size is first created
#Variables for indicating the top row, bottom row, left column and right column is initiated with values 0, size-1, 0, size-1 respectively
#A variable for the value to be placed at each location is intialized with a value 1
#Check whether the given size is zero. If yes return the matrix which is a null matrix
#The values are to be inserted till the vallue is equal to the square of the given size which can be done using a loop which runs till the value to be inserted is leass than or equal to the square of the given size. This is achieved using a while(True) which runs till the value to be inserted is greater than the square of the given size
#Values are added are from the first column till the last column of the topmost row. After the rightmost column of the topmost row next value is to be added to the rightmost column of the rows below the topmost row. So the variable holding the topmost row value is incremented by 1
#Values are added to the rightmost columns of the next row till the last row. After the value is added to rightmost column of the bottommost row next value is to be added to the column before the rightmost column of the bottommost row. So the variable holding the rightmost row value is decrmented by 1
#Values are added to the column to the left of the rightmost column of the last row till the last column of the last row. After the value is added to leftmost column of the bottommost row next value is to be added to the leftmost columns of the rows above the bottommost row. So the variable holding the bottommost row value is decrmented by 1
#Values are added to the leftmost columns of the row above the bottommost row to the topmsot row. After the value is added to leftmost column of the topmost row next value is to be added to the column after the leftmost column of the topmost row. So the variable holding the leftmost row value is incrmented by 1
def spiral_matrix(size):
    spyral_matrics=[row[:] for row in [[0]*size]*size] #Initializes a 2D matrix of zeros of given size
    left = 0 #Intializes the variable to indicate leftmost column
    right = size-1 #Intializes the variable to indicate rightmost column
    top = 0 #Intializes the variable to indicate topmost row
    bottom = size-1 #Intializes the variable to indicate bottommost row
    value = 1 #Intializes the variable for the value to be placed at each position
    
    if size == 0: #Checks whether the given size is zero
        return spyral_matrics
        
    while(True): #Initilaises an indefinite while loop
        if value > size*size: #Checks whether the value to be inserted is greater than the square of the given size
            break #Breaks the loop
        for kolum in range(left,right+1): #Iterates across the columns of the topmost row from left to right
            spyral_matrics[top][kolum] = value #The zeros are replaced by the values
            value += 1 #Increments the value variable
        top += 1 #Increments the value of the topmost row variable
        for raw in range(top,bottom+1): #Iterates across the rightmost columns of the next row till the last row
            spyral_matrics[raw][right] = value #The zeros are replaced by the values
            value += 1 #Increments the value variable
        right -= 1 #Decrements the value of the rightmost column variable
        for kolum in range(right,left-1,-1): #Iterates across the columns of the bottommost row from column to the left of the leftmost column to the leftmost column
            spyral_matrics[bottom][kolum] = value #The zeros are replaced by the values
            value += 1 #Increments the value variable
        bottom -= 1 #Decrements the value of the bottommost row variable
        for raw in range(bottom,top-1,-1): #Iterates across the leftmost columns of the row above the bottommost row till the topmost row
            spyral_matrics[raw][left] = value #The zeros are replaced by the values
            value += 1 #Increments the value variable
        left += 1 #Increments the value of the leftmost column variable      
    return spyral_matrics #Returns the spiral matrix