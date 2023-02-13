#Maximum d'une liste

l=[1,900,34,654,7,897,9]
i=0
maxi=l[0]
while i<len(l):
    if maxi<l[i]:
        maxi=l[i]
    i=i+1
print(maxi)
