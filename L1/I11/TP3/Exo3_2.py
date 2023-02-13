s=input("Saisir une chaine de caracteres: ")
i=0
j=len(s)-1
while i<=j and s[i]==s[j]:
    i=i+1
    j=j-1
if i>j:
    print("C'est un palindrome")
else :
    print("Le mot n'est pas un palindrome")
