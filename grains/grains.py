def square(number):
    try:
        if number in range(1,65):
            return 2**(number-1)
        else:
            raise ValueError("square must be between 1 and 64")
    except ValueError as e:
        print(e)
        raise
    
def total():
    sum=0
    for number in range(1,65):
        count=2**(number-1)
        sum+=count
    return sum
