def tobase2(n):
    L = []
    while n != 0 :
        L = [n & 1] + L
        n = n>>1
    return L

print(tobase2(23))
