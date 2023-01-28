
def prime(number):
    if number<1:
        raise ValueError('there is no zeroth prime')
    else:
        prime_numbers=[2]
        num=3
        while len(prime_numbers)<number:
            for p in prime_numbers:
                if num%p==0:
                    break
            else:
                prime_numbers.append(num)
            num+=1
        return prime_numbers[-1]
        
        
        
                
                    
               
    

    
                

    
