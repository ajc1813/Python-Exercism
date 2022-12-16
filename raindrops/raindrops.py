def convert(number):
    sound=""
    if number%3==0:
        if number%5==0 and number%7==0:
            return sound+"Pling"+"Plang"+"Plong"
        elif number%5==0:
            return sound+"Pling"+"Plang"
        elif number%7==0:
            return sound+"Pling"+"Plong"
        else:
            return sound+"Pling"
    elif number%5==0:
        if number%7==0:
            return sound+"Plang"+"Plong"
        else:
            return sound+"Plang"
    elif number%7==0:
        return sound+"Plong"
    else:
        return str(number)
