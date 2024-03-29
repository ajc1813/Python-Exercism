"""Functions to automate Conda airlines ticketing system."""

#def generate_seat_letters(number):
    #"""Generate a series of letters for airline seats.

    #:param number: int - total number of seat letters to be generated.
    #:return: generator - generator that yields seat letters.

    #Seat letters are generated from A to D.
    #After D it should start again with A.

    #Example: A, B, C, D

    #"""

    #pass

#def generate_seats(number):
    #"""Generate a series of identifiers for airline seats.

    #:param number: int - total number of seats to be generated.
    #:return: generator - generator that yields seat numbers.

    #A seat number consists of the row number and the seat letter.

    #There is no row 13.
    #Each row has 4 seats.

    #Seats should be sorted from low to high.

    #Example: 3C, 3D, 4A, 4B

    #"""

    #pass

#def assign_seats(passengers):
    #"""Assign seats to passengers.

    #:param passengers: list[str] - a list of strings containing names of passengers.
    #:return: dict - with the names of the passengers as keys and seat numbers as values.

    #Example output: {"Adele": "1A", "Björk": "1B"}

    #"""

    #pass

#def generate_codes(seat_numbers, flight_id):
    #"""Generate codes for a ticket.

    #:param seat_numbers: list[str] - list of seat numbers.
    #:param flight_id: str - string containing the flight identifier.
    #:return: generator - generator that yields 12 character long ticket codes.

    #"""

    #pass

#A dictionary of seat letters is defined first. As per test data , letters used are A, B, C and D corresponding to the numbers 1,2,3,4 respectively. If number is greater than 4, then it should be converted into a number between 1 and 4. This is done by finding the remainder obtained when the number is divided by 4 which is the frequency of the letters. Since multipliers of 4 gives a remainder of 0, the letter corresponding to 0 is also 'D' in addition to the 1
seat_letter_dict={0:'D',
                  1:'A',
                  2:'B',
                  3:'C',
                  4:'D'} #Creates a dictionary for seat letters

def generate_seat_letters(number):
    for num in range(1,number+1): 
        yield seat_letter_dict[num%4]

#A generator object which holds the the required no:of seat letters is first generated using the function generate_seat_letters()
#Row number should be appended to left side of seat letters in each row which starts from 1. To find the row associated with a seat, first calculate the quotient obtained when the index of the seat in the object holding seat letters is divided by 4. For each row, quotient will be one less than the row number. For example seats in the first row, quotient obtained will be zero while for seats in the second row, quotient obtained will be one and so on. So the row number, which is appended to the seats in a row is obtained by adding one to the quotient obtained. But the number 13 is skipped which means from row 13 onwards, the row number is two more than the quptient. Since seat letter is a string and row number is integer, row number is first converted to a string using the str() function and then appended to the left side of the seat letter 
def generate_seats(number):
    seat_letter = generate_seat_letters(number) #Creates a generator object which holds the required no:of seat_letters
    for index,letter in enumerate(seat_letter):
        row_number = index//4 #Find the quotient obtained by dividing index of seat letter in the generator object by 4
        if row_number < 12: #Checks whether the row is less than 13
            yield str(row_number+1)+letter #Appends one more than the quotient to the beginning of the seat letter
        else:
            yield str(row_number+2)+letter #Appends two more than the quotient to the beginning of the seat letter

#A empty dictionary is created for the seat assignment
#A gnerator object holding the seats are generated using the generate_seats() function. For each passenger, a seat should be allotted which means that the number of passengers and no:of seats are equal. For this the number of passengers is found which is equal to the length of the list 'passengers' which holds the names of all the passengers. The exact no:of seats are generated by passing the no:of passengers as the parameter of the function generate_seats() function. Thus a generator object holding the seats and a list holding pasengers are available. Now passenger and seat at corresponding index are added as a key-value pair to the dictionary for seat assignment
def assign_seats(passengers):
    ceat_assignment = {} #Initializes a dictionary indictaing the seat assignment
    number = len(passengers) #Finds the number of passengers
    ceat_no = generate_seats(number) #Creates a generator object containing exactly same no:of seats as the number of passenegers
    for index,ceat in enumerate(ceat_no):
        ceat_assignment[passengers[index]] = ceat #Adds the passenger name and seat assigned to the dictionary
    return ceat_assignment #returns the seat assignment dictionary

#For obtaing the ticket code, the flight_id is appended to the end of the seat number. Since the ticket code length should be 12, zeros are appended to the end of the string obtained by concatenating the seat number and flight_id using the ljust() function
def generate_codes(seat_numbers, flight_id):
    for num in seat_numbers:
        yield (num+flight_id).ljust(12, '0')
