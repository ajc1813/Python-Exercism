     
def find(search_list, value):
    low=0
    high=len(search_list)-1
    while low<=high:
        mid=(low+high)//2
        if value<search_list[mid]:
            high=mid-1
        elif value>search_list[mid]:
            low=mid+1
        else:
            return mid
    else:
        raise ValueError("value not in array")
        

        
