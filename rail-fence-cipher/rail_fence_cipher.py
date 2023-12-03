#def encode(message, rails):
    #pass

#def decode(encoded_message, rails):
    #pass

#A variable for the row with initial value 0, a list whose length is equal to the length of the message and a variable for direction are initialized. The direction variable indicates whether to move up or down in rows 
#For a character in the message if the current row is the first row or topmost row, then next character should be placed below the current row i.e. the direction variable should point downwards. For a character in the message if the current row is the last row or bottommost row, then next character should be placed babove the current row i.e. the direction variable should point upwards
#If the direction variable is pointing downwards increment the row variable else decrement the row variabe
def encode(message, rails):
    l = len(message) #Finds the length of the message
    encoded_list = [""for x in range(l)] #Creates a list of null characters whose length is equal to length of the message
    row = 0 #Creates a variable for the row number
    if rails == 1: #Checks whether the number of rows is one
        return message #returns the message    
        
    for i in range(l): #Iterates across the characters in the message
        encoded_list[row] += message[i] #Places the character the row specified by the row variable
        if row == rails-1: #Checks whether the row is the bottommost row
            down = False #Assigns value 'False' to the direction variable
        elif row == 0: #Checks whether the row is the topmost row
            down = True #Assigns value 'True' to the direction variable
       
        if down: #Checks whether the direction variable is True
            row += 1 #Increments the row variable by 1
        else:
            row -= 1 #Decrements the row variable by 1
            
    encoded_list = list(filter(None,encoded_list)) #Removes the empty characaters in the list
    return ''.join(encoded_list) #Joins the list elements to form a string which is the encoded string and it is returned

def decode(encoded_message, rails):
    memory = [[] for i in range(rails)]
    msg = list(encoded_message)
    count = {i: 0 for i in range(rails)}
    rail = 0
    for i in range(len(msg)):
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        count[rail] += 1
        rail += direction
    j = 0
    for i in range(rails):
        memory[i].extend(msg[j:j + count[i]])
        j += count[i]
    result = []
    rail = 0
    for i in range(len(msg)):
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = - 1
        result.append(memory[rail].pop(0))
        rail += direction
    return ''.join(result)
            
'''
length_dict = {
               2:2,
               3:4,
               4:6,
               5:8
              }
def encode(message, rails):
    encoded_message = ''
    raw_string = ''
    group_length = length_dict[rails]
    message_list = [(message[i:i+group_length]) for i in range(0, len(message), group_length)]
    maxLen = max(map(len, message_list))
    equi_length_list = [row + ('@'*(maxLen - len(row))) for row in message_list]
    new_list = [i[1:] for i in equi_length_list]
    for string in equi_length_list:
        encoded_message += string[0]
    middle = round(rails/2)
    if (rails%2 == 0) and rails > 2:
        for i in range(middle+1):
            for string in new_list:
                raw_string = string[i] + string[-(i+1)]
                set_string = set(raw_string)
                if len(set_string) == 1:
                    encoded_message = encoded_message + "".join(set(set_string))
                else:
                    encoded_message = encoded_message + raw_string

    else:
        for i in range(middle):
            for string in new_list:
                raw_string = string[i] + string[-(i+1)]
                set_string = set(raw_string)
                if len(set_string) == 1:
                    encoded_message = encoded_message + "".join(set(set_string))
                else:
                    encoded_message = encoded_message + raw_string
    return encoded_message.replace('@','')
'''    
'''
2 - 2
3 - 4
4 - 6
5 - 8
'''
'''
XOXOXOXOXOXOXOXOXO

X . X . X . X . X . X . X . X . X 
. O . O . O . O . O . O . O . O . O
'''

'''
3
W . . . E . . . C . . . R . . . L . . . T . . . E  2*2
. E . R . D . S . O . E . E . F . E . A . O . C .  2*1
. . A . . . I . . . V . . . D . . . E . . . N . .  2*2
0 1 2 3 4 5 6 7 8 9

'''

'''
EXERCISES
4
E . . . . . S . . . . .
. X . . . I . E . . . @
. . E . C . . . S . @ .
. . . R . . . . . @ . .
0 1 2 3 4 5 6 7 8
'''