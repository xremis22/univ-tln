#Question 1
def factorielle(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorielle(5))

#Question 2
def TrianglePascal(n) :
    coef=n+1
    p=[0]*(n-1)
