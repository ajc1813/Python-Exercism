#class Luhn:
    #def __init__(self, card_num):
        #pass
        
    #def valid(self):
        #pass

class Luhn:
    def __init__(self, card_num):
        self.card_num=card_num.replace(" ","") #Removes spave from the card number

    def valid(self):
        if self.card_num.isdigit(): #Checks whether the card number has non-digits
            if len(self.card_num)<=1:
                return False
            else:
                double_list=[] #initializes an empty list for the list after doubling
                num_list=list(self.card_num) #Converts the card number intoa list in which each element is a string
                num_list=[int(x) for x in num_list] #Converts the list of strings to a list of integers
                num_list.reverse() #Reverses the list as digits are considered from right for doubling
                for i in range(len(num_list)): #iterates overs the length of the list
                    digit=num_list[i]
                    if i%2==0: #Checks whether the index position is even
                        double_list.append(digit) #Appends the value at the index position to the list after doubling
                    else:
                        digit*=2 #Doubles the element at the index position
                        if digit>9: #Checks whether the element is greater than 9 after doubling
                            digit=digit-9 #Subtracts 9 from the digit
                            double_list.append(digit) #Appends the value at the index position to the list after doubling
                        else:
                            double_list.append(digit) #Appends the value at the index position to the list after doubling                 
                s=sum(double_list) #Find the sum of list elements
                return s%10==0


        else:
            return False