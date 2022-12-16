def square_of_sum(number):
    sum_1=0
    for x in range(number+1):
        sum_1+=x
    return pow(sum_1,2)
        
def sum_of_squares(number):
    sum_2=0
    for x in range(number+1):
        sum_2+=pow(x,2)
    return sum_2
        
def difference_of_squares(number):
    return square_of_sum(number)-sum_of_squares(number)
