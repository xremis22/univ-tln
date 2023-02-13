#Maximum d'une liste 2

l=[1,12,34,6504,7,897,9]
i=1
maxi1=l[0]
maxi2=l[0]
while i<len(l):
    if maxi1<l[i]:
        maxi2=maxi1
        maxi1=l[i]
    elif l[i]>maxi2:
        maxi2=l[i]
    i=i+1
print(maxi1,maxi2)
