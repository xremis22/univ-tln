def sous_groupe_gen(b,f):
# defintion du cours sur les groupes
# <b> = {b, b*b, b*b*b, ...., e}
# où ici l'opérateur * est la multiplication dans F_2^m
# et e = 1
        L = [b]
        a = multiplication(b,b,f)
        while a!=b :
            L += [a]
            a = multiplication(a, b, f)
        return L
        
def ordre(b,f):
# definition du cours
# ordre(b) = card(<b>)
    return len(sous_groupe_gen(b,f))
    

def symetrique_mul(x,P):
# dans F_2^m le symetrique de alpha^i est alpha^(2^m-1-i)
# car alpha^(2^m-1) = 1
# cf. question (4) du TD3
    m = len(bin(P)) - 3
    i = log_table[x]
    return alpha_table[((1 << m)-1)-i]

def is_sym_mul(b,c,f):
# version où dispose de la multiplication
# on verifie alors que b*c = 1 dans le corps
 return multiplication(b,c,f)==1
 
def is_sym_mul(b,c,f):
# version où l'on dispose des tables log
# si b = alpha^i et c = alpha^j alors
# c est le symétrique de b si i+j = 0 modulo 2^m-1
# point abordé lors de la question 5 de l'exercice 1 du TD3
    m = len(bin(f))-3
    return (b!=0) and (c != 0) and ((log_table[c] + log_table[b]) % ((1<<m) -1))==0
