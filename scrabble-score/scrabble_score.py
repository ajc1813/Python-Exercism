#A set in which each key-value pair represents a lower case alphabet and its score and a variable for score is defined
#The set is defined for lower case alphabets. But word may contain upper case letters which causes error. So word is converted to lower case
#Next iteration is done over the letters in the 'word'. Value corresponding to each letter is obtained from the set and added to the acore variable
#After iteration is over the score is returned

def score(word):
    alphabet_score= {'a': 1,
                     'b': 3,
                     'c': 3,
                     'd': 2,
                     'e': 1,
                     'f': 4,
                     'g': 2,
                     'h': 4,
                     'i': 1,
                     'j': 8,
                     'k': 5,
                     'l': 1,
                     'm': 3,
                     'n': 1,
                     'o': 1,
                     'p': 3,
                     'q': 10,
                     'r': 1,
                     's': 1,
                     't': 1,
                     'u': 1,
                     'v': 4,
                     'w': 4,
                     'x': 8,
                     'y': 4,
                     'z': 10
} #Defines a set in which each key-value pair represents a lower case alphabet and its score
    scrabble_score=0 #initializes a variable
    word=word.lower() #Converts 'word' to lower case
    for word in word: #iterates over letters in 'word'
        scrabble_score+=alphabet_score[word] #Adds the value corresponding to the letter to the variable representing the acore
    return scrabble_score #returns the scrable score