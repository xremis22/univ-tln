#Maximum d'une liste 3

l=[1,12,34,6504,7,897,9]
i=1
maxi1=l[0]
maxi2=l[0]
indice1=0
indice2=0
while i<len(l):
    if maxi1<l[i]:
        maxi2=maxi1
        indice2=0
        maxi1=l[i]
        indice1=i
    elif l[i]>maxi2:
        maxi2=l[i]
        indice2=i
    i=i+1
print(maxi1,maxi2)
print(indice1,indice2)
