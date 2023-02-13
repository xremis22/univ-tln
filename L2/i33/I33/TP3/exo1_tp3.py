def tobase2(n):
    L = []
    while n != 0 :
        L = [n%2] + L
        n = n//2
    return L
n = 22 & 21

print(tobase2(n))
print(tobase2(n&(n-1)))
