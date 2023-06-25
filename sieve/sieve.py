def primes(limit):       
    num_list = list(range(limit+1))
    prime = []
    for i in num_list:
        c = 0
        for j in range(1,i):
            if i%j == 0:
                c += 1
        if c == 1:
            prime.append(i)
    return prime