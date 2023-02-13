def ord(a, n):
    res = n
    while(n!=0):
        a, n = n, a%n
    return res/a
