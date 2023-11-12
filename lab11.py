#presume ledder is put upright against a wall let variable length and angle store the length of ladder and the angle form with the ground as it leans against the wall.
#wap to compute the hieght reached by ladder on the wall if lenght of the lladder is 16 feet and angle is 75 degree 
import math
len=float(input("Enter the lenght="))
angle=float(input("Enter the angle in degree="))
angrad=math.radians(angle)
height=len*math.sin(angle)
print("height reached=",height)