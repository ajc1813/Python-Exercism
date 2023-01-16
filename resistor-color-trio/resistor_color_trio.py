#A set in which each key-value pair represent a colour and its corresponding value is defined
#The values of the first two bands are concatenated and zeros are added to the left end of this concatenated value according to the value of the third band
#If a group of three consecutive zeros at the trailing end are present, then unit used is kiloohms else unit is ohms
def label(colors):
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
    } #Creates a set in which each key-value pair represent a colour and its corresponding value
    band_1=colour_values[colors[0]] #Obtains the value of the first band
    band_2=colour_values[colors[1]] #Obtains the value of the second band
    band_3=colour_values[colors[2]] #Obtains the value of the third band
    sum=str(colour_values[colors[0]])+str(colour_values[colors[1]]) #Concatenates the values of the first and second bands. if 'str' is not used, instead of concatenation, addition will occur
    resistance_value=sum.ljust(band_3 + len(str(sum)), '0') #Add zeros according to the value of the third band 
    if resistance_value[-3:]=='000': #Checks whether group of three consecutive zeros are present at the end of the resistance value
        return resistance_value[:-3]+" "+"kiloohms"
    else:
        return resistance_value+" "+"ohms"
