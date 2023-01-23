#def slices(series, length):
    #pass

def slices(series, length):
    if length==0:
        raise ValueError("slice length cannot be zero")
    elif length<0:
        raise ValueError("slice length cannot be negative")
    elif len(series)==0:
        raise ValueError("series cannot be empty")
    elif len(series)<length:
        raise ValueError("slice length cannot be greater than series length")
    else:
        i=0
        substring_list=[]
        while i<=(len(series)-length):
            substring=series[i:i+length]
            substring_list.append(substring)
            i+=1
        return substring_list
    