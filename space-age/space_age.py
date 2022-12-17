#Approach to solve this exercise is as follows. Consider a test case. For example in the test case for eartn it is given "SpaceAge(1000000000).on_earth(), 31.69". Consider "SpaceAge(1000000000).on_earth()" SpaceAge is the class. "SpaceAge(1000000000).on_earth()" means class name followed by a dot which is followed by function call. This denotes the instance method discussed in the "Ellen's Alien Game" exercise. So this exercise is solved using instance method in class
#Solution to this exercise is as follows. The age in years on earth  i.e. earth_age is calculated from seconds by multipying the seconds by 1/60/60/24/365.25(which is the fomula for converting seconds to years). Age in years on any other planet i.e. space age is obtained by dividing the earth age by the orbital period of that planet. Since the result contains only two decimal points, the space age is rounded to two decimal points using the round() function

class SpaceAge:
    def __init__(self, seconds):
        self.earth_age=seconds/60/60/24/365.25 #Creates the instance property "earth_age" 

    #Instance method for calculating age in years on earth
    def on_earth(self):
        space_age=self.earth_age
        return round(space_age,2)

    #Instance method for calculating age in years on mercury
    def on_mercury(self):
        space_age=self.earth_age/0.2408467
        return round(space_age,2)

    #Instance method for calculating age in years on venus
    def on_venus(self):
        space_age=self.earth_age/0.61519726
        return round(space_age,2)  

    #Instance method for calculating age in years on mars
    def on_mars(self):
        space_age=self.earth_age/1.8808158
        return round(space_age,2) 

    #Instance method for calculating age in years on jupiter
    def on_jupiter(self):
        space_age=self.earth_age/11.862615
        return round(space_age,2)

    #Instance method for calculating age in years on saturn
    def on_saturn(self):
        space_age=self.earth_age/29.447498
        return round(space_age,2)

    #Instance method for calculating age in years on uranus
    def on_uranus(self):
        space_age=self.earth_age/84.016846
        return round(space_age,2)

    #Instance method for calculating age in years on neptune
    def on_neptune(self):
        space_age=self.earth_age/164.79132
        return round(space_age,2)        
    
        
