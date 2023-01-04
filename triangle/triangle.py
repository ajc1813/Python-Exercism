def equilateral(sides):
    return sides[0]==sides[1]==sides[2]!=0
def isosceles(sides):
    if sides[0]+sides[1]>sides[2] and sides[1]+sides[2]>sides[0] and sides[2]+sides[0]>sides[1]: #Checks whether the triangle is a valid triangle
        return sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2]
    else:
        return False
 
def scalene(sides):
    if sides[0]+sides[1]>sides[2] and sides[1]+sides[2]>sides[0] and sides[2]+sides[0]>sides[1]: #Checks whether the triangle is a valid triangle
        return sides[0]!=sides[1] and sides[0]!=sides[2] and sides[1]!=sides[2]
    else:
        return False