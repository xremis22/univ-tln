#https://www.commentcamarche.net/contents/217-le-chiffrement-de-vigenere

def vigenere_chiffre(f_in, f_out, cle) :
    i = 0
    result = ""
    for i in range(len(f_in)) : #dans le fichier
        lettre = f_in[i]
        if lettre != " " : #si il y a un espace, ne rien faire
            lettre = lettre.lower() #mettre en minuscule
            let_ord = ord(lettre) #transformer la lettre en int
            i = (i + 1)%len(cle) #s'assurer que i ne dépasse pas (car len(cle) peut être > à len(f_in))
            let_ord += (ord(cle[i]) - ord('a'))%26
            result += chr(let_ord) #transformer la lettre en str
            f_out.write(result) #écrire le résultat
            i = (i + 1)%len(cle) #s'assurer que i ne dépasse pas (car len(cle) peut être > à len(f_in))
        #else :
            #result += "."
    print(result)
    f_in.close()
    f_out.close()
    return f_out

"""def vigenere_dechiffre(f_in, f_out, cle) :
    i = 0
    result = ""
    for i in range(len(f_in)) :
        chiffr = f_in[i]
        if chiffr != "." :
            chf_ord = ord(chiffr)
            i = (i+1)%len(cle)
            chf_ord += (ord('a') - ord(cle[i]))%26
            result += chr(chf_ord)
            f_out.write(result)
            i = (i+1)%len(cle)
        #else :
            #result += " "
    print(resulf_outt)
    return f_out"""

def vigenere_dechiffre(source, destination, cle) :
    ligne = ""
    source = open(f_in, "r")
    destination = open(f_out,"w")
    n=len(cle)
    k=0
    L=""
    C=""
    for ligne in source :
        L=ligne
        C=cle
        ns=len(L)
        M=""
        LM=['']*ns

        for i in range(0,ns) :
            LM[i]+=chr(((((ord(L[i]))-97)-((ord(C[k%n]))-97))%26)+97) #M
            M+=LM[i]
            k=k+1
        M+=('\n')
        destination.write(M)
    source.close()
    destination.close()

def main() :
    cle = "bbbbb"
    f_in = open('crypto_vigenere',"r")
    f_in = f_in.read()
    f_out = open('rspnc.txt', "w")
    print("Le chiffrement : \n")
    print(vigenere_chiffre(f_in, f_out, cle))
    print("Le dechiffrement : \n")
    print(vigenere_dechiffre(f_in, f_out, cle))

#print(main())


mot_cle = "fdlsfr"
k = 0
while k <= len(mot_cle) :
    ord_let = ord(mot_cle[k])
    print(ord_let)
    k += 1
