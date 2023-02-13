def tobase(n,b):
    L = []
    while n != 0 :
        L = [n%b] + L
        n = n//b
    return L

print(tobase(25,8))
