import math
def score(x, y):
    s=math.sqrt(pow(x,2)+pow(y,2))
    if s<=1:
        return 10
    elif 1<s<=5:
        return 5
    elif 5<s<=10:
        return 1
    else:
        return 0
           
