from pocketnoobj import *

ch=input ("Saisir une chaine de caracteres: ")
nch=""
i=0
while i<len(ch):
    if ch[i]!=' ':
        nch+=ch[i]
    i+=1
print(nch)
