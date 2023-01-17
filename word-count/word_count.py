#The sentence is first converted to lower case using lower() function and the following symbols are removed from it (",","\n",":","_","!!&@$%^&",".","\t") using replace() function and single quotes at the beginning and end of the sentence is removed using strip() function(The single quotes symbols also should be removed which may occur at the beginning or end of the sentence or words in the sentnce or within letters like "can't" and "don't". If single quotes are removed using replace() function, then it will also remove single quotes in the letters which will cause error. So single quotes inside the sentence are not removed at this stage)
#The sentence is then converted to a list using the split() function
#The list contains empty characters corresponding to the replaced symbols and words in the string.The empty elements are removed and a new list is formed
#An empty list is created for removing the single quotes at the begining and end of words within the sentence and an empty dictionary is created to calculating the word count
#The single quotes at the begining and the end of the words in the sentence is removed. For that iteration is done over the words in the list obtained from the sentence. The single quotes at the begining and the end of the word is removed using strip() function. The word without single quotes at the begining and the end is added to list created for removing the single quotes at the begining and end of words within the sentence
#Word count is done now. For that iteration is done over the words in the new list. Count of each word is found using the count() function and the word and its count is added as a key-value pair to a dictionary created for count
def count_words(sentence):
    sentence_list=sentence.lower().replace(","," ").replace("\n","").replace(":","").replace("_"," ").replace("!!&@$%^&","").replace(".","").replace("\t"," ").strip("'").split(" ") #Converts the sentence to lower case and removes symbols from it and then converts it into a list
    sentence_list = [x for x in sentence_list if x != ''] #Removes the empty elements in the list corresponding to replaced symbols and a new list is formed
    new_sentence_list=[] #Initializes an empty list for removing the single quotes at the begining and end of words within the sentence 
    count_dict=dict() #Initializes an empty dictionary for calculating the word count
    for word in sentence_list: #Iterates over the words in the list obtained from the sentence
        word=word.strip("'") #Removes single quotes at the begining and the end of the word
        new_sentence_list+=[word] #Adds the word without single quotes at the begining and the end is added to list created for removing the single quotes at the begining and end of words within the sentence
    for new_word in new_sentence_list: #Iterates over the words in the new list obtained
        count=new_sentence_list.count(new_word) #Counts the occurence of the word in the list
        count_dict[new_word] = count #Adds the word and its count to the dictionay created for count
    return count_dict