# Globals for the directions
# Change the values as you see fit
#EAST = None
#NORTH = None
#WEST = None
#SOUTH = None

#class Robot:
    #def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        #pass
#The values for the directions ar assigned such to obtain the direction after turning right, multiply by -i and to obtain the direction after turning left, multiply by i
#In the test, it is given "robot.move("R"), self.assertEqual(robot.coordinates, (0, 0)),  self.assertEqual(robot.direction, EAST)". This means that the class 'Robot' has two attributes 'coordinates' and 'direction' and a method 'move'
#The north and south directions are associated with the imaginary axis while westa nd east are associated with real part of direction. To incrtement corresponding to an advance movement, add the corresponding coordinate by the value of the real or imaginary part associated with the direction
EAST = 1
NORTH = 1j
WEST = -1
SOUTH = -1j

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.x_coordinate=x_pos
        self.y_coordinate=y_pos
        self.coordinates=(self.x_coordinate,self.y_coordinate)
        self.direction=direction

    def move(self,path):
        for step in path:
            if step=='A':
                self.x_coordinate+=self.direction.real #Increments the x coordinate by the value of real part of the direction
                self.y_coordinate+=self.direction.imag #Increments the y coordinate by the value of imaginary part of the direction
                self.coordinates=(self.x_coordinate,self.y_coordinate)       
            if step=='R':
                self.direction=self.direction*complex(0,-1) #Multiplies the seld.direction by -i
            elif step=='L':
                self.direction=self.direction*complex(0,1)  #Multiplies the seld.direction by i          