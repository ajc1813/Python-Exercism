def two_fer(name=""):
    l=len(name)
    if l==0:
        return f"One for you, one for me."
    elif l!=0:
        return f"One for {name}, one for me."
    else:
        return None
