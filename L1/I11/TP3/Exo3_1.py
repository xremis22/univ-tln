s=input("Saisir une chaine de caracteres: ")
i=0
j=len(s)-1
while i<=j:
    if i!=j:
        print(s[i]+s[j])   
    else:
        print(s[i])
    i=i+1
    j=j-1    

