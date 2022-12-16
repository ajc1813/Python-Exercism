import string
def is_pangram(sentence):
    l=len(sentence)
    new_sentence=sentence.translate(str.maketrans('', '', string.punctuation)) 
    sentence_list=new_sentence.lower().replace(" ","").replace("_","")
    new_list = [item for item in sentence_list if not item.isdigit()]
    

    
    
    alphabets=set('abcdefghijklmnopqrstuvwxyz')
    if l>=26:
        if len(set(list_lower))==26:
            return True
        elif len(set(list_lower))<26:
            return False 
    else:
        return False


        
            
            
        
