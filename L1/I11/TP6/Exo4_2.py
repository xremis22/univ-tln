from pocketgl import *
init_window("Trace de fonctions",700,500)
current_color("gray")
for i in range(0,7):
    line(50+i*100,0,50+i*100,500,2)
for i in range(0,5):
    line(0,50+i*100,700,50+i*100,2)
current_color("black")
line(350,0,350,500,2)
line(0,250,700,250,2)

