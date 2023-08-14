#class Clock:
    #def __init__(self, hour, minute):
        #pass

    #def __repr__(self):
        #pass

    #def __str__(self):
        #pass

    #def __eq__(self, other):
        #pass

    #def __add__(self, minutes):
        #pass

    #def __sub__(self, minutes):
        #pass

#The given hour is converted into 24-hour format if it is greater than 24. This is done by modulud operator which returns the difference between the greatest multiple of 24 below the given hour and the hour. For example if hour is 100, then difference between 100 and 96 is taken
#If the given minute is greater than 60, then it should converted to hour-minute format. The minute can be found using modulus operator. To find the corresponding hour, find the difference between the given minute and the largest multiple of the 60 below the given minute. This gives a multiple of 60 which is converted to hours using integer division operator. The hours obtained by conversion of minutes is added to the hour. This sum can be greater than 24. So modulo operator is again used
#__str__ method, the human radeable format of the time is returned i.e. hour and minute are represented as a zero-padded decimal number. For example if time is 9 hours and 9 minutes, the time is represented as 09.09. For this a string is formed using the hour and minutes. This string is converted to datetime object using strptime() function. Here the format codes used are %H and %M which represents hour and minutes as zero-padded decimals. the result of the strptime() function consisits of date(day, month, year) and time(hour, minute, second) out of which only hour and minute are required. So the output of strptime() function is sliced
#In the __eq__ method(), two clocks are compared
#In the __add__ method(), the given minutes is added to the clock. Note that the minutes.minute is not required as it will cause error
#In the __sub__ method(), the given minutes is added to the clock. Note that the minutes.minute is not required as it will cause error

from datetime import datetime
class Clock:
    def __init__(self, hour, minute):
        self.hour = ((hour % 24) + ((minute - (minute % 60))//60)) % 24 #Obtains hour in 24-hour format
        self.minute = minute % 60 #Obtains minute in 60 minute format
        self.time = ""

    def __repr__(self):
        return 'Clock(' + str(self.hour) + ','+ ' ' + str(self.minute) + ')' #Returns the string format of the clock class

    def __str__(self):
        self.time = str(self.hour) + ':' + str(self.minute) 
        return str(datetime.strptime(self.time, "%H:%M").time())[0:5] #Returns the string format of the given time
        
    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute #Check whether the given clocks are equal

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes) #Returns the sum of the given minutes and the clock

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes) #Returns the difference of the clock and the given minutes
