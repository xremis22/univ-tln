#Module vecteur
#AJAMI BOUSTAJI Sammer
#09 décembre 2019

#(2)
u=[1,1]
v=[5,-1]
def somme_vect(u,v):
    s=[]
    for i in range(len(u)):
        s+=[u[i]+v[i]]
    return s
print(somme_vect(u,v))

def diff_vect(u,v):
    d=[]
    for i in range(len(u)):
        d+=[u[i]-v[i]]
    return d
print(diff_vect(u,v))

#(3)

def prod_scal(u,v):
    p=0
    for i in range(len(u)):
        p+=u[i]*v[i]
    return p
print(prod_scal(u,v))

#(4)

m=[(1,0),(1,1)]
def prod_mat_vec(u,m):
    pmv=0
    for i in range(len(m)):
        for k in range(len(m[i])):
            pmv+=u[i]*m[i](k)
    return pmv
print(prod_mat_vec(u,m))

