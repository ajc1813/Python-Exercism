#While checking for even and odd numbers, check whether  number%2==0. it true number is even otherwise number is odd. Do not use number%3==0 for checking as it is correct for certain even numbers also. Example is 12

def steps(number):
    step_count=0
    if number <1:
        raise ValueError("Only positive integers are allowed")
    else:
        if number==1:
            return step_count
        else:
            while number>1:
                number=number//2 if number%2==0 else (3*number)+1
                step_count+=1
            return step_count


    
        


