def ens_to_int(A):
    t = 0
    B2 = {}
    i = 0
    while(i<=len(A)):
        B2[A[i]] += [1]
        i += 1
    return B2

A = {2, 5, 8, 9}
print(ens_to_int(A))
