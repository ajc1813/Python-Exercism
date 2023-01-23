#def recite(start_verse, end_verse):
    #pass
#The characteristics of the carol is as follows. Each verse can be obtained from the previous verse by replacing the day name in the first part of the verse(i.e. part before colon symbol) and adding an additional gift along with 'and' in the beginning of the second part of the verse
#Solution of the exercise is as follows
#Two dictionaries are created:-one for day numbers and second one for gifts
#A function to create a verse when the verse number is given is defined first. From the second verse an 'and' is required. Since first verse does not require 'and' it is created directly
#For creating second verses onwards, first a list is created. The first element of the list is the firt part of the verse in which day number is choosen from the first dictionary whose key is equal to the start_verse. The second element is the first value from the dictionary of gifts with 'and' at the beginning. The verses are created by adding gifts, corresponding to second key till the key equal to the start_verse, at the second position of the list i.e. at index 1. Thus nth verse is formed by joining the value corresponding to the  first n values from the second dictionary. List is used because in the result a sting in list ois required. If additions are done at the end or beginning, the string can be used. But here additions are to be done inside the string. So string is used
#If the starting verse and ending verse are same it means that only one verse is to returned. This can be obtained by just calling the function for creating a verse when verse number is given
#When starting verse and ending verse are not same, it means that verses from the starting verse to the ending verse should be returned. For this and empty set is created for the carol. Then verse corresponding to each verse in the range (start_verse,end_verse+1) is obtained(Here one is added to end_verse because range function will increment only upto one less than the maximum range value i.e. end_verse-1 in this case. But verse including that corresponding to end_verse is required. So simply using end_verse in the range function will cause error). Then the verses are added to the set for carol

day={1:'first',
     2:'second',
     3:'third',
     4:'fourth',
     5:'fifth',
     6:'sixth',
     7:'seventh',
     8:'eighth',
     9:'ninth',
     10:'tenth',
     11:'eleventh',
     12:'twelfth'} #Creates a dictionary for day number. Since r
gift={1:'a Partridge in a Pear Tree.',
      2:'two Turtle Doves,',
      3:'three French Hens,',
      4:'four Calling Birds,',
      5:'five Gold Rings,',
      6:'six Geese-a-Laying,',
      7:'seven Swans-a-Swimming,',
      8:'eight Maids-a-Milking,',
      9:'nine Ladies Dancing,',
      10:'ten Lords-a-Leaping,',
      11:'eleven Pipers Piping,',
      12:'twelve Drummers Drumming,'} #Creates a dictionary for gifts

#The function for creating a verse when the verse number is given is defined below. 
def verse(start_verse): #Creates a function to define a verse if the verse number is given
    if start_verse==1: #Checks whether the verse is first verse
        verz=[f"On the first day of Christmas my true love gave to me: ",f"a Partridge in a Pear Tree."] #First verse is defined
        return ["".join(verz)] #Joins the contents of the list 'verz' to a string and place the string in a list
    else:
        verz=[f"On the {day[start_verse]} day of Christmas my true love gave to me:",f' and a Partridge in a Pear Tree.'] #Creates a list for verse
        i=2 #Initialises a variable 
        while i<=start_verse: #Iterates over the gifts to be added
            verz.insert(1,f' {gift[i]}') #Adds each gift at index i
            i+=1 #Increments the variable
        return ["".join(verz)] #Joins the contents of the list 'verz' to a string and place the string in a list   
        
def recite(start_verse, end_verse):
    if start_verse==end_verse: #Checks whether only one verse is to recited
        return verse(start_verse) #Creaes the carol
    else:
        carol=[] #Initialises an empty set for carol
        for i in range(start_verse, end_verse+1): #Iterates over the starting verse to the ending verse
            carol+=verse(i) #Adds verse corresponding to the verse number 'i' to set for carol
            i+=1 #Increments the variable
        return carol        

        
        


