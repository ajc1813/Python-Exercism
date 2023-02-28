#def recite(start, take=1):
    #pass

#The characteristics of the song is as follows. Every verse is identical except that the numbers are different. The number corresponding to start begins from 10 and decreases by one for the following verse till one is reached. In the first two lines of each verse, the number corresponding to the verse is used and in the last line of each verse, one less than the number in the first two lines is used. Also numbers in the beginning of a line starts with a capital letter and those inside starts starts with a small letter. Thus numbers in the first lines starts with capital letters and number in last line is a small letter. Also if number is one, the term 'bottle' should be used after one otherwise 'bottles' are used
#Solution of the exercise is as follows
#Two dictionaries are created:-one for number corresponding to the start and second for the term 'bottle'
#A function to create a verse corresponding to a given 'start' is defined first. In the first two lines, value of the key whose value is equal to the 'start' is used for numbers and in the last line, value of the key whose value is equal to the one less than 'start' is used for numbers. Since the value obtained for the number starts with capital letter but in the last line, small case is used. So the value obtained from the dictionary is converted into small case using lower() function. The 'bottle' or 'bottles' is selcted from the second dictionary according to the value of the start
#if only one verse is required, it is obtained using the function for creating the verse
#If multiple verse are required, the 'take' no:of verses starting from the 'start' value is choosen and added with a null element between them. After all the verses are added, the final eleemnt will be null element which is removed to obtain the required bottle song
count={0:"no",
       1:'One',
       2:'Two',
       3:'Three',
       4:'Four',
       5:'Five',
       6:'Six',
       7:'Seven',
       8:'Eight',
       9:'Nine',
       10:'Ten'
    } #Creates a dictionary for number
bottle_count={0:'bottles',
              1:'bottle',
              2:'bottles',
              3:'bottles',
              4:'bottles',
              5:'bottles',
              6:'bottles',
              7:'bottles',
              8:'bottles',
              9:'bottles',
              10:'bottles'}
def verse(start):
    verz=[f"{count[start]} green {bottle_count[start]} hanging on the wall,",f"{count[start]} green {bottle_count[start]} hanging on the wall,", f"And if one green bottle should accidentally fall,",f"There'll be {count[start-1].lower()} green {bottle_count[start-1]} hanging on the wall."] #Creates a verse
    return verz
    
def recite(start, take=1):
    if take==1: #Checks whether the value of 'take' is one
        return verse(start) #returns verse corresponding to the start
    else:
        bottle_song=[] #Initializes an empty list for the song
        for i in range(take): #Iterates over the range of take
            bottle_song+=verse(start-i) #Obtains the verse corresponding to (start-i) and adds ita n element of the list for song
            bottle_song.append("") #Adds a null element after the verse in the list for bottle song      
        return bottle_song[:-1] #Removes the last null element