#def factors(value):
    #pass
      
def factors(value):
    prime_factors = []
    factor = 2
    while value > 1:
        while value % factor == 0:
            value = value / factor
            prime_factors.append(factor)
        factor += 1
    return prime_factors