def response(hey_bob):
    if len(hey_bob)==0:
        return "Fine. Be that way!"
    else:
        if hey_bob.isupper():
            if hey_bob[-1]!="?":
                return 'Whoa, chill out!'
            else:
                return "Calm down, I know what I'm doing!"
        elif hey_bob.isspace():
            return 'Fine. Be that way!'
        else:
            if hey_bob[-1]=="?":
                return "Sure."
            elif hey_bob[-1]==" ":
                if hey_bob[-4]==" ":
                    return 'Whatever.'
                else:
                    return "Sure."
            elif hey_bob[-1]=="\t":
                return 'Fine. Be that way!'
            else:
                return 'Whatever.'










































        
    