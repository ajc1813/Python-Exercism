#Square root of a radicand is a number which when multiplied by itself yields the radicand. Also a number is completely divisible by its square root
#A variable is initialised whose value lies between one and the radicand
#The variable is iterated over the above range
#If a value of the variable satifies the conditions of square root mentioned in the first line, then it is the square root
def square_root(number):
    sqrt=1 #initializes a variable for square root
    while sqrt<number: #Checks whether the variable is less than the number
        if number%sqrt==0 and sqrt*sqrt==number: #Checks whetehr the radicand is completely divisible by the value of the variable and product of the value of the variable with itself gives the radicand
            break #If above condition is satisfied it means that the value variable is the sqaure root of the radicand. So no further looping is required which menas the loop has to be exited which is done by the break statement
        sqrt+=1 #Increments the value of the variable by one when the if condition is satisifed
    return sqrt #returns the sqaure root after loop is exited when break statement is encountered
    