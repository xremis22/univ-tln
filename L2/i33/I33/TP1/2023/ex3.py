def pgcd(a, b):
    if(b==0):
        return a
    else :
        c = a%b
        return(pgcd(b, c))


def somme(L, M):
    R = [0, 0]
    R_ = [0, 0]
    res = 0
    while(res==0):
        if(L[1]==M[1]): #Ici on vérifie si les dénominateurs sont égaux
            R[0] = L[0] + M[0]
            R[1] = L[1]
        else : #Dénominateurs différents
            R[1] = L[1]*M[1]
            R[0] = L[0]*M[1] + M[0]*L[1]
        if(R[0]%R[1]==0): #Ici on vérifie si la fraction peut s'écrire en int
            res = R[0]//R[1]
            return res
        else :
            R_[0] = R[0]
            R_[1] = R[1]
            R[0] = R[0]//pgcd(R_[0], R_[1])
            R[1] = R[1]//pgcd(R_[0], R_[1])
            
