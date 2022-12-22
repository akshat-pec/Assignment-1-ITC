import math
angle = int(input("Enter a angle: "))
while(angle<=345):
    r=math.radians(angle)
    sine=round(math.sin(r),4)
    cosine=round(math.cos(r),4)
    print(angle , sine , cosine)
    angle = angle+15