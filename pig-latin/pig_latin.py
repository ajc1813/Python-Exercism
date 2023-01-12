#A list of vowels is first created which includes a,e,i,o.,u,xr,yt
#The text is checked for space
#if no space is present that means only one word is present in the text. 
#If no space is present, it is checked whether the first letter of the word or first two letters of the word belongs to the list of vowels. If yes 'ay' is added at the end of the word
#If the text contains no space and the first letter of the word or first two letters of the word belongs to the list of vowels, then there are three cases:-Substring 'qu' is present in the word, 'y' is the second or third letter of the word, words without wither of the previous two cases. 
#If substring 'qu' is present in the string, then the text is divided into two parts:-first part consists of the text upto u and secons part consisits of portion of the text after 'u'. Then first part is added to the end of the scond part and the string 'ay' is added at the end of the concatenated string
#if y is the second or thirs element of the text is divided into two parts:-first part consists of the text before 'y' and second part consisits of portion of the text from 'y'. Then first part is added to the end of the scond part and the string 'ay' is added at the end of the concatenated string
#In the third case, the text is divided into two parts:-first part consists of the text before the vowel and second part consisits of portion of the text from the vowel. Then first part is added to the end of the scond part and the string 'ay' is added at the end of the concatenated string
#if the text contains space, it means that multiple words are present in the text. So the text is parsed using split() function with spcae as delimiter
#An empty list is created
#Iteration is done over th elements of the list
#If the substring 'qu' is present in the word, then perform the same operation as mentioned in the case of no space present in the text and substring 'qu' is present. The changed word is then added to the empty string
#If the substring 'qu' is not present in the word, then perform the same operation as mentioned in the case of no space present in the text and first letter is not a vowel. The changed word is then added to the empty string
#The result obtained in the above two cases is a list which is converted to a string using join() function

vowels=['a','e','i','o','u','xr','yt'] #Creates a list of vowels
def translate(text):
    if " " not in text: #Checks whether space is present in the text
        if text[0] in vowels or text[:2] in vowels: #Checks whether the first letter of the word or first two letters of the word belongs to the list of vowels
            return text+'ay' #Adds the 'ay' substring to the text
        else:
            if 'qu' in text: #Checks whether the substing 'qu' is present in the text
                u_index=text.index('u') #Obtains the index of 'u' in the text
                return text[(u_index+1):]+text[:(u_index+1)]+'ay' #Obtains a concatenated string by adding portion of the text after letter 'u' , portion of the text upto 'u' and 'ay'
            elif text[1]=='y' or text[2]=='y': #Checks whether 'y' is the second or third letter of the text
                y_index=text.index('y') #Obtains the index of 'y' in the text
                return text[y_index:]+text[:y_index]+'ay' #Obtains a concatenated string by adding portion of the text from letter 'u' , portion of the text before 'u' and 'ay'
            else:
                for vowel_index, letter in enumerate(text):
                    if letter in vowels: #checks whether the letter is in the list of vowels
                        return text[vowel_index:]+text[:vowel_index]+'ay'  #Obtains a concatenated string by adding portion of the text before the vowel , portion of the text from the vowel and 'ay'       
    else:
        result=[] #Creates an empty list
        for word in text.split(" "): #Iterates over the words in the text
            if 'qu' in word: #Checks whether the substring 'qu' is present in the word
                u_index=word.index('u') #Obtains the index of 'u' in the text
                result+=[word[(u_index+1):]+word[:(u_index+1)]+'ay'] #Adds the modified word to the empty string
            else:
                for index, letter in enumerate(word):
                    if letter in vowels: #checks whether the letter is in the list of vowels
                        result+=[word[index:]+word[:index]+'ay'] #Obtains a concatenated string by adding portion of the text before the vowel , portion of the text from the vowel and 'ay' which is stored in the empty list
        return " ".join(result) #Converts the list to a string