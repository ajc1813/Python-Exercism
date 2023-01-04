def is_valid(sides):
    sides.sort
    if sides[0] + sides[1] >= sides[2]:
      return True
    return False
    
def equilateral(sides):
    return sides[0]==sides[1]==sides[2]!=0

def isosceles(sides):
    return is_valid(sides) and (sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2])
 
def scalene(sides):
    if sides[0]+sides[1]>sides[2] and sides[1]+sides[2]>sides[0] and sides[2]+sides[0]>sides[1]: #Checks whether the triangle is a valid triangle
        return sides[0]!=sides[1] and sides[0]!=sides[2] and sides[1]!=sides[2]
    else:
        return False
        
