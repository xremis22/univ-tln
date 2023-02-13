from random import *
i=0
L=[0,0,0,0,0,0,0,0,0,0,0]
while i<=10000:
    de=randrange(0,6)+randrange(0,6)
    L[de]=L[de]+1
    i=i+1
print(L)

from pocketgl import *
init_window('histogramme',250,1000)
a=0
for i in range(11):
    current_color(randrange(0,255),randrange(0,255),randrange(0,255))
    box(a+10,0,a+30,L[i]//2)
    a=a+20
    
