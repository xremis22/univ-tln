#TD3
#Exo2

ch=input("Saisisez une chaine de caracteres : ")
i=0
chv=" "
cpt=0
while i<len(ch):
    if ch[i]==chv:
        cpt=cpt+1
    i=i+1
print(cpt)



i=0
ch2=""
for i in ch:
    if i=="a":
        ch2+=str(4)
    else :
        ch2+=i

i=0
ch2=""
while i<len(ch):
    if ch[i]=="a":
        ch2+="4"
    else :
        ch2+=ch[i]
    i+=1
print(ch2)
