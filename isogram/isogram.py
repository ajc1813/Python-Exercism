def is_isogram(string):
    string=string.lower().replace(" ","").replace("-","")
    if len(string)==len(set(string)):
        return True
    else:
        return False
    
