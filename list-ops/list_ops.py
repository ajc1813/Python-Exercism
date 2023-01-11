def append(list1, list2):
    return list1+list2

def concat(lists):
    concatenated_list=[]
    for element in lists:
        concatenated_list+=element
    return concatenated_list

def filter(function, list):
    result=[]
    for element in list:
        if element%2==1:
            result+=[element]
    return result
            
def length(list):
    length=0
    for element in list:
        length+=1
    return length
    
def map(function, list):
    result=[]
    for element in list:
        element+=1
        result+=[element]
    return result

def foldl(function, list, initial):
    if len(list)==0:
        return initial
    else:
        result=initial
        for i in range(len(list)):
            result+=list[i]
        return result
        
def foldr(function, list, initial):
    if len(list)==0:
        return initial
    else:
        result=initial
        for i in range(len(list)):
            result=list[(len(list)-1)-i]+result
        return result

def reverse(list):
    reversed_list=[]
    l=len(list)
    for i in range(l):
        reversed_list+=[list[(l-1)-i]]
    return reversed_list
        
        
