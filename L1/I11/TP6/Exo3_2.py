from random import *
from pocketgl import *
init_window('Quart de cercle',1000,1000)
current_color(0,0,0)
circle(0,0,1000)
i=0
n=0
m=0
o=0
while i<1000000:
    x,y=random(),random()
    dist=(x**2+y**2)**(1/2)
    if dist<1:
        n=n+1
        current_color("green")
        point(x*1000,y*1000)
    elif dist>1:
        m=m+1
        current_color("red")
        point(x*1000,y*1000)
    else :
        o=o+1
        current_color("black")
        point(x*1000,y*1000)
    i=i+1
print("points dans le cercle:",n)
print("points sur le cercle:",o)
print("points dehors le cercle",m)
main_loop()
