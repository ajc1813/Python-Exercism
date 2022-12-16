def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquot_sum=0
    if number>0:
        for x in range(1,number):
            if number%x==0:
                aliquot_sum+=x
        if aliquot_sum<number:
            return "deficient"
        elif aliquot_sum==number:
            return "perfect"
        elif aliquot_sum>number:
            return "abundant"
    else:
        raise ValueError("Classification is only possible for positive integers.")
