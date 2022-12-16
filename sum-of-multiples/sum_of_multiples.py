def sum_of_multiples(limit, multiples):
    multiples_set=set()
    for number in multiples:
        if number!=0:            
            for x in range(limit):
                if x%number==0:
                    multiples_set.add(x)
    return sum(multiples_set)
