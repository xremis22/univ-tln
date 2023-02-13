def pgcd(a,b):
    c=0
    while b>a :
        c=a
        a=b
        b=c
    if b==0:
        return a
    else :
        reste=a%b
        return pgcd(b,reste)

print(pgcd(39,15))
