#def encode(numbers):
    #pass

#def decode(bytes_):
    #pass

#An empty list is initialized for the enoded value
#The input numbers is a list and iteration is done over the list
#If the list element is less than or equal to 127, then encoded value is the same. So input itself is returned
#If the list element is gretaer than 127, then it is converted into binary which has a prefix '0b'. To remove it, slicing is done. Then the binary value is grouped into group of 7 bits starting from the left. The rightmost group may sometimes less than 7bits. In such case, length of all groups are made 7 by appending zeros at the end using ljust() function. Now sign bit is to be added. For this 1 is added to the starting of all the bit groups. But sign bit of the rightmost group is zero. So it is replaced by 0. Now a list of bit gorups of length 8 is ready. Next each bit group is converted into corresponding decimal which is then added to the list for the ecoded output
def encode(numbers):
    encoded_list = [] #Initializes an empty list for the enocded output
    for bite in numbers:
        if bite <= 127: #Checks whether the list element is less than or equal to 127
            encoded_list.append(bite) #Appends the list element to the list for encoded output
        else:
            bynary = bin(bite)[2:] #Converts the list element into corresponding binary
            bynary_list = [bynary[max(i-7,0):i] for i in range(len(bynary), 0, -7)][::-1] #Converts the binary into groups
            bynary_equal_list = [str(i).rjust(7, '0') for i in bynary_list] #Make the length of all bit groups into 7
            bynary_new_list = [str(i).rjust(8, '1') for i in bynary_equal_list] #Prefix 1 to all the bit groups as sign bit
            bynary_new_list[-1] = '0'+bynary_equal_list[-1] #Makes the sign bit of the rightmost bit group '0'
            integer_list = [int(elt,2) for elt in bynary_new_list] #Converts the bit group into decimal
            encoded_list.extend(integer_list) #Appends the list of decimal values to the list for encoded output
    return encoded_list #Returns the encoded output

def decode(bytes_):
    if len(bytes_) > 0 and bytes_[-1] & 0x80 > 0:
        raise ValueError('incomplete sequence')
    number, num_lst = '', []
    for byte in bytes_:
        binary = bin(byte)[2:]
        if len(binary) == 8:
            number += binary[1:]
        else:
            number += '0' * (7 - len(binary)) + binary
            num_lst.append(int(number, 2))
            number = ''
    return num_lst
