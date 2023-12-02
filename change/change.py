#def find_fewest_coins(coins, target):
    #pass

#From the test data, we can see that the output required is in a list format. So an empty list is initialized for the change output
#When target is negative, ValueError is raised and when target is zero, an empty list is returned
#Last case is positive target whose different cases are exlained below
#If the target is less than the samllest coin which is the first element of the coin list, ValueError is raised
#If the target cannot be made with the coins given, ValueError is raised 
#If target is present in the coins list, it is appended to the empty list for change using append() function else check whether target can be expressed as the sum of coins given using a function. If not check whether the target can be achieved using elbonian coins i.e. target is a multiple of a given coin. If not express the traget in terms of liliputian coins
def find_fewest_coins(coins, target):
    change = [] #Initializes an empty list for the change
    coins_sum = sum(coins) #Calculates the sum of the list of coins
    if target < 0: #Checks whether the target is negative
        raise ValueError("target can't be negative") #Raises ValueError
    elif target == 0: #Checks whether the target is zero
        return change #Returns the empty list
    else:
        if (target < coins[0]): #Checks whether the target is less than the smallest coin
            raise ValueError("can't make target with given coins") #Raises ValueError
        if (coins[0] != 1) and (coins_sum < target) and (target%coins_sum != 0): #Checks whether the target can be made with the coins given
            raise ValueError("can't make target with given coins") #Raises ValueError   
        if target in coins: #Checks whether the target is in the given coins 
            change.append(target) #Apends the traget to the list for the change
        else:
            sum_check_flag , change = multiple_coin_check(coins, target) #Obtains the flag that indicates whether target can be achieved using multiple coins and the changes by calling the function for checking multiple coins
            if sum_check_flag == 0: #Checks whether the target can be achieved using multiple coins
                elbonia_check_flag , change = elbonia_coin_check(coins, target) #Obtains the flag that indicates whether target can be achieved using elbonian coins and the changes by calling the function for checking elbonian coins
                if elbonia_check_flag == 0: #Checks whether the target can be achieved using melbonian coins
                    change = lilliputian_coin_check(coins, target)  #Obtains the liliputian coins that adds upto the target using a function for calculating the liliputian coins           
    return change #Returns the change

  
#Function for checking whether target can be achieved using multiple coins. list
#An empty list for the change and a flag for indicating whether target can be achieved using multiple coins are initialized
#In this function each coin is added with all other coins. If sum of any two coins gives the target the flag is made 1 and the coins are appended to the list for the output using append() function
def multiple_coin_check(coins, target):
    change = [] #Initializes an empty list for the output
    sum_check_flag = 0 #Initializes a flag to indicate whether target is the sum of multiple coins
    for i in range(len(coins)): #Iteartes across the given coins
        for j in range(i+1, len(coins)): #Iterates across the coin other than selected in the above loop
            if coins[i] + coins[j] == target: #Checks whether sum of two coins is equal to target
                sum_check_flag = 1 #Updates the flag value to 1 if traget is sum of two coins
                change = change + [coins[i] , coins[j]] #Appends the coins to the output list
    return sum_check_flag , change #Returns the flag value and the change list


#Function for checking whether target can be achieved using elbonian coins
#An empty list for the change and a flag for indicating whether target can be achieved using elbonian coins are initialized  
#In this function, whether target is a multiple of any coin is checked. Since any number is a multiple of 1, 1 should be avoided during checking. If yes the flag value is updated to 1 and the coin is added to the output list. From the test data, we can see that coin is added a value equal to the multiplying value. So the coin is duplicated 
def elbonia_coin_check(coins, target):
    change = [] #Initializes an empty list for the output
    elbonia_check_flag = 0 #Initializes a flag to indicate whether target is a multiple of a coin
    for i in range(len(coins)): #Iteartes across the given coins
        if target%coins[i] == 0 and coins[i] != 1: #Checks whether the target is a multiple of a coin ither than unit coin
            elbonia_check_flag = 1 #Updates the flag value to 1 if traget is multiple of a coin
            change.append(coins[i]) #Appends the coin to the output list
            multiplier = target//coins[i] #Calculates the no:of times coins contains in the traget
            change = change*multiplier #Appends the elbonian coin multiple times to the output list
    return elbonia_check_flag , change #Returns the flag value and the change list


#Function for checking whether target can be achieved using elbonian coins
#Since only coins whose sum is less than the target are used, a list of those coins are obtained. for this sum of elements of the coin list starting from left is calculated. Only those coins whose sum is less than the target is obtained
#Check whether the first coin in the list of coins whose sum is less than target is unit coin
#If yes find how many times each coin(say it is n), beginning from the largest coin, contains in the target value using floor division and add that coin to the output list n times. Then subtract highest multipler of coin in the traget from the target. For example coin list is  and target is 999. Here check_list [1, 2, 5, 10, 20, 50, 100]. First largest value which is 100 is considered. 100 contains 9 times in 999. So 100 is appended 9 times to the output list. Then 900 is subtracted from 999 which gives 99. Next value is 50 which contains one time in 99. So 50 is appended one time and it is reduded from 99 giving 49 and os on
#If no, the output is obtained as follows. Consider the example of coin list [4, 5] and target 27 and output is [4, 4, 4, 5, 5, 5]. Here check_list is [4,5]. Output containes 4 and 5. Here the sum of check_list is 4+5=9 and target is 27. Differenc is 27-9 = 18. 18 is taken as new target. This 18 should be expressed in terms of 4 and 5. Here as done in the yes case cannot be done. Here we are starting with the larger number i.e. 5 is subtracted from new target 18 which gives 13. If the difference is greater than the sum of the remaining elements in the check_list(i.e. 4) and zero, add the number to the output list. Continue till this condition si satisfied. When condition is false, take the next number an drepeat the process  
def lilliputian_coin_check(coins, target):
    check_list = [] #Initializes a list for coins whose sum is less than the target
    change = [] #Initializes an empty list for the output
    num_list = []
    for coin in coins: #Iteartes across the given coins
        if sum(check_list+[coin]) <= target: 
            check_list.append(coin) #Appends the coin to the list for coins whose sum is less than target
    if check_list[0] == 1: #Checks whether the first coin is unity coin
        for num in check_list[::-1]: #Iteartes across the coins in check list in the descending order
            multiplier = target//num #Fibd how many times the coin contains in the target
            num_list = [num]*multiplier #Form a list of the coin in which coin is repeated
            change = num_list + change #Appends the coin to the output list
            target = target - (num*multiplier) #Subtract the highest multiplier of the coin in the target from the traget
        return change #Return the change
    else:
        new_target = target - sum(check_list) #Obtains a new target value
        new_check_list = [item for item in check_list if item < new_target] #Obtains a new check list
        for num in new_check_list[::-1]: #Iteartes across the coins 
            new_list = [item for item in new_check_list if item < num] #Creates a list that contains all elements in the check list other than the number
            indx = check_list.index(num) #Find the index of the number
            check_list[indx:indx] = [num] #Adds the number to the index position so that similar numbers are together
            new_sum = sum(new_list) #Iteartes across the coins in check list in the descending order
            if new_target-num >= new_sum and new_target-num >= 0: # Check whether difference of the new target and number is greater than or equal to the new sum and zero
                check_list[indx:indx] = [num] #Appends the number to the output list    
                new_target= new_target - num #Subtracts the number from the new target
        return check_list