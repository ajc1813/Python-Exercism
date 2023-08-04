#def resistor_label(colors):
    #pass

#Two dictionaries are first created:- one in which each key-value pair represent a colour and its corresponding value and second in which each key-value pair represent a colour and corresponding tolerance value
#If only one band is present "0 ohms" is returned
#Else the values of the the bands, multipler and tolerance is found accorsing to the length of the bands. The values are then concatenated. The values are integers and so they are first converted to strings using str() function and the concatenated using '+' symbol. If they are not converted to strings instead of concatenation, addition will takes place. Then zeros are added to this string according to the multipler value and then the string is converted to integer using int() function. This gives the resistance. Then reistance is modified and to it units(as per the test data) and tolerance are concatenated. Since resistance and tolernace are integers, for concatenating they are converted to string using str() function
def resistor_label(colors):
    colour_values={'black': 0,
            'brown': 1,
            'red': 2,
            'orange': 3,
            'yellow': 4,
            'green': 5,
            'blue': 6,
            'violet': 7,
            'grey': 8,
            'white': 9
    } #Creates a dictionary in which each key-value pair represent a colour and its corresponding resistance value

    tolerance={'grey': 0.05,
               'violet': 0.1,
               'blue': 0.25,
               'green': 0.5,
               'brown': 1,
               'red' : 2,
               'gold': 5,
               'silver': 10
              } #Creates a dictionary in which each key-value pair represent a colour and corresponding tolerance value
    
    if len(colors) == 1:
        return "0 ohms"
    elif len(colors) == 4:
        value_1=colour_values[colors[0]] #Obtains the value corresponding to the first band
        value_2=colour_values[colors[1]] #Obtains the value corresponding to the second band
        multiplier=colour_values[colors[2]] #Obtains the multipler
        tolerance=tolerance[colors[3]] #Obtains the tolerance
        sum=str(value_1)+str(value_2) #Concatenates the values of the first and second bands
    elif len(colors) == 5:
        value_1=colour_values[colors[0]] #Obtains the value corresponding to the first band
        value_2=colour_values[colors[1]] #Obtains the value corresponding to the second band
        value_3=colour_values[colors[2]] #Obtains the value corresponding to the third band
        multiplier=colour_values[colors[3]] #Obtains the multiplier
        tolerance=tolerance[colors[4]]
        sum=str(value_1)+str(value_2)+str(value_3) #Concatenates the values of the first, second and third bands
    resistance_value=int(sum.ljust(multiplier + len(sum), '0')) #Adds zeros according to the mulplier value
    if resistance_value > 100000: #Checks whether resistance is greater than 100000
        return str(resistance_value/1000000).rstrip('.0')+" "+"megaohms"+" "+"±"+str(tolerance)+"%"
        #Returns the resistance value. After division by 100000, results with decimal parts will be obtained. As per test data if deimal part ontains only zero, then deimal part should be avoided otherwise it should be kept. Deimal part can be avoided by using int() function. But in some test cases, non-zero deimal parts are present(7.3) whih also gets removed causing error. So zeros are removed using rstrip() funtion
    elif resistance_value > 1000 and resistance_value < 100000: #Checks whether resistance is between 1000 and 100000
        return str(resistance_value/1000).rstrip('.0')+" "+"kiloohms"+" "+"±"+str(tolerance)+"%" #Returns the resistance value   
    else:
        return str(resistance_value)+" "+"ohms"+" "+"±"+str(tolerance)+"%" #Returns the resistance value