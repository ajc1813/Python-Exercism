def is_armstrong_number(number):
    sum=0
    l=len(str(number))
    for digit in str(number):
        digit_power=int(digit)**l
        sum+=digit_power
    if sum==number:
        return True
    else:
        return False
