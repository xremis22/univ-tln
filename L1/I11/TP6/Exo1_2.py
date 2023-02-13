from pocketgl import *
init_window('Degrade de gris',500,500)
i=0
a=0
c=0
while i<50:
    current_color(c,c,c)
    box(0,a,500,a+10)
    c=c+5
    a=a+10
    i=i+1
main_loop()
