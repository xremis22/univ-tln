from random import *

i=0
n=0
m=0
o=0
N=100000
while i<N:
    x,y=random(),random()
    dist=(x**2+y**2)**(1/2)
    if dist<1:
        n=n+1
    elif dist>1:
        m=m+1
    else :
        o=o+1
    i=i+1
print("pi=",(4*n/N))
        
