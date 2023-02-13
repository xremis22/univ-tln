#Création des listes

l=[]
som=0
n=int(input())
while n!=0:
    l=l+[n]
    som=som+n
    n=int(input())
print(l,len(l),som)

