def table_alpha(P):
    degree_poly = len(bin(P))-3
    nbr_elements = (1<<degree_poly) -1
    L     = [0]*nbr_elements
    L[0]  = 1
    alpha = 1
    i     = 1
    while i < nbr_elements:
        alpha = multbyalpha(alpha,2,P)
        L[i] = alpha
        i+=1
    return L
def multiplie(b, c, f):
  res = 0
  t = b
  k = c
  while t != 0:
    if (t & 1) != 0:
      res ^= k
    k = multbyalpha(k,f)
    t = t >> 1
  return res

def multbyalpha(b, f):
  t = b << 1
  n = len(bin(f)) - 3
  if t & (1<<n) != 0:
    return t^f
  else:
    return t
def table_log(P):
  liste_log = [-1,0,1]
  r = len(bin(P))-3
  elements = 1 << r
  j = 0
  while j < elements - 3:
    liste_log.append(0)
    j += 1
  i = 1
  exp = 1
  while i < elements -1 :
    exp = multbyalpha(exp,P)
    liste_log[exp] = i
    i += 1
  return liste_log
print(table_log(13))

def evalue(Q,y,P):
    res = Q[0]
    for i in range(1,len(Q)):
        res = multiplie(res,y,P)^Q[i]
    return res
print(evalue([4,3,6], 2, 13))

def inverse(x,P):
    degree_poly = len(bin(P))-3
    nbr_elements = (1<<degree_poly) -1
    alpha = log_table[x]
    alpha = alpha<<(nbr_elements-1)
    return alpha_table[alpha]

def decompose(n):
    listePremier = []
    cpt = 0
    if n%2 == 0:
        while n%2 == 0:
            n = n//2
            cpt +=1
        listePremier += [[2,cpt]]
    i = 3
    while n != 1 :
        if n%i == 0 :
            cpt = 0
            while n % i == 0 :
                n = n // i
                cpt+=1
            listePremier += [[i,cpt]]
        i += 2
    return listePremier

def decomposebin(n):
    L = []
    while n != 0:
        L.insert(0,n&1)
        n = n >> 1
    return L
print(decomposebin(23))

def element_median(A):
  L = []
  n = len(A)
  for i in range(n):
    for j in range(n):
      L.append(A[i][j])
  
  L = sorted(L)
  index = ((n**2) // 2) 
  return L[index]

print( 	element_median([[9, 9, 4], [9, 0, 1], [6, 3, 2]]),
        element_median([[6, 8, 4], [7, 0, 3], [9, 0, 1]]),
        element_median([[6, 3, 6], [5, 7, 0], [5, 7, 0]]),
        element_median([[5, 9, 5], [6, 6, 5], [5, 5, 5]]),
        element_median([[8, 5, 9, 6, 4], [1, 4, 5, 3, 9], [2, 4, 3, 7, 1], [5, 0, 9, 3, 8], [5, 7, 5, 3, 8]]),
        element_median([[9, 5, 4], [9, 7, 8], [8, 9, 3]]),
        element_median([[8, 6, 2], [7, 1, 5], [0, 3, 9]]),
        element_median([[9, 3, 6, 2, 6], [0, 0, 3, 9, 2], [7, 7, 9, 2, 7], [4, 0, 4, 6, 8], [6, 5, 6, 8, 6]]),
        element_median([[2, 4, 4, 6, 1], [9, 1, 8, 6, 3], [7, 9, 3, 5, 6], [2, 0, 5, 4, 3], [5, 3, 6, 1, 1]]),
        element_median([[4, 6, 1, 3, 5], [5, 1, 6, 8, 8], [2, 7, 3, 0, 9], [0, 2, 8, 9, 0], [1, 4, 3, 7, 7]])	
)


def det_Z26(A):
    all_pivot = 1
    for i in range(len(A)-1):
        pivot = A[i][i]
        #Calcul de pivot et permutation
        if pivot%2 == 0 or pivot % 13 == 0:
          i_piv = i
          while (pivot % 2 == 0 or pivot % 13 == 0) and i_piv < len(A):
              pivot = A[i_piv][i]
              i_piv += 1
          if pivot % 2 == 0 or pivot % 13 == 0  :
            return 0
          else : 
            tmp = A[i]
            A[i] = A[i_piv-1]
            A[i_piv-1] = tmp
            all_pivot *= -1
        
        for j in range(i+1, len(A)):
            all_pivot *= pivot
            all_pivot %= 26
            pivot2 = A[j][i]
            A[j][i] = pivot * pivot2 - pivot2 *  pivot
            A[j][i] %= 26
            for  k in range(i+1, len(A)):
                A[j][k] = pivot * A[j][k] - pivot2 * A[i][k]
                A[j][k] %= 26
    det = 1
    for i in range(len(A)):
        det *= A[i][i]
        det %= 26
    return (det * pow(all_pivot,11,26)) % 26

def print_matrice(M):
  for i in range(len(M)):
    print(M[i])
  print("\n")

A = [ [3, 7, 5],
      [4, 2, 6],
      [1, 10, 9]]
print(det_Z26(A))

def det(A):
    all_pivot = 1
    for i in range(len(A)):
        pivot = A[i][i]
        #Calcul de pivot et permutation
        if pivot == 0:
          i_piv = i
          while pivot == 0 and i_piv < len(A):
              pivot = A[i_piv][i]
              i_piv += 1
          if pivot == 0 :
            return 0
          else : 
            tmp = A[i]
            A[i] = A[i_piv-1]
            A[i_piv-1] = tmp
            all_pivot *= -1
        
        for j in range(i+1, len(A)):
            all_pivot *= pivot
            pivot2 = A[j][i]
            A[j][i] = pivot * pivot2 - pivot2 *  pivot
 
            for  k in range(i+1, len(A)):
                A[j][k] = pivot * A[j][k] - pivot2 * A[i][k]

    det = 1
    for i in range(len(A)):
        det *= A[i][i]
    return det/all_pivot
def print_matrice(M):
  for i in range(len(M)):
    print(M[i])
  print("\n")

A = [ [-3,2,-1,4],
      [0,3,0,-5],
      [1,0,-4,3],
      [0,3,3,0] ]
print(det(A))

def print_matrice(M):
  for i in range(len(M)):
    print(M[i])
  print("\n")

def gauss(A):
    diag = min(len(A),len(A[0]))
    for i in range(diag):

        pivot = A[i][i]
        #Calcul de pivot et permutation
        if pivot == 0:
          i_piv = i
          while pivot == 0 and i_piv < len(A):
              pivot = A[i_piv][i]
              i_piv += 1
          if pivot == 0 :
            return (A,False) 
          else : 
            tmp = A[i]
            A[i] = A[i_piv-1]
            A[i_piv-1] = tmp
       
        for j in range(i+1, len(A)):
            pivot2 = A[j][i]
            A[j][i] = pivot * pivot2 - pivot2 *  pivot
            for k in range(i+1, len(A[0])):
                A[j][k] = pivot * A[j][k] - pivot2 * A[i][k]
    return(A, true)
    
    
 
def nature(A):
  print_matrice(A)
  n = len(A)
  p = len(A[0])
  famille_gen   = int((n >= p) and gauss(A)[1])
  famille_libre = int((n <= p) and gauss(A)[1])
  nature = (famille_gen, famille_libre) 
  return nature

def print_matrice(M):
  for i in range(len(M)):
    print(M[i])
  print("\n")
  

def resolution(A, b):
  result = [1]*len(b)
  result[0] = b[0]/A[0][0]
  # print(result)
  for i in range(1,len(A)):
    res = 0
    for j in range(i):
      res += A[i][j]*result[j]
    result[i] = (b[i]-res)/A[i][i]
    # print(result,i, b[i], res)
  return result

def resolution2(A, b):
  n = len(b)
  result = [1]*n
  result[n-1] = b[n-1]/A[n-1][n-1]
  # print(result)
  for i in range(1,len(A)):
    res = 0
    for j in range(i):
      res += A[-i-1][-j-1]*result[-j-1]

    result[-i-1] = (b[-i-1]-res) / A[-i-1][-i-1]
  return result

def det(A):
    all_pivot = 1
    for i in range(len(A)):
        pivot = A[i][i]
        #Calcul de pivot et permutation
        if pivot == 0:
          i_piv = i
          while pivot == 0 and i_piv < len(A):
              pivot = A[i_piv][i]
              i_piv += 1
          if pivot == 0 :
            return 0
          else : 
            tmp = A[i]
            A[i] = A[i_piv-1]
            A[i_piv-1] = tmp
            all_pivot *= -1
        
        for j in range(i+1, len(A)):
            all_pivot *= pivot
            pivot2 = A[j][i]
            A[j][i] = pivot * pivot2 - pivot2 *  pivot
 
            for  k in range(i+1, len(A)):
                A[j][k] = pivot * A[j][k] - pivot2 * A[i][k]

    det = 1
    for i in range(len(A)):
        det *= A[i][i]
    return det/all_pivot
    
 
 
 def multbyalpha(b, f):
  t = b << 1
  n = len(bin(f)) - 3
  if t & (1<> 1
  return res
def matmat_f(A,B,P):
  C = []
  for i in range(len(A)):
    L = []
    for j in range(len(B[0])):
      res = 0
      for k in range(len(B)):
        res ^= multiplie(A[i][k],B[k][j],P)
      L.append(res)
    C.append(L)
  return C
  
 
import random
def gentrianginf_inv(n, t):
    L = []
    for i in range(n):
      sous_liste = [0]*n
      for j in range(i):
        sous_liste[j] = random.randrange(0,t)
      sous_liste[i] = random.randrange(1,t)
      L.append(sous_liste)
    return L
 
 
 
import random
def gentrianginf_mod26(n):
   L = []
   for i in range(n):
     sous_liste = [0]*n
     for j in range(i):
       sous_liste[j] = random.randrange(0,26)
     x = random.randrange(0,26)
     while x%2 == 0 or x%13 == 0:
       x = random.randrange(1,26)
     sous_liste[i] = x
     L.append(sous_liste)
   return L


 def transpose(M):
    L = []
    for i in range(len(M[0])):
        sous_liste = []
        for j in range(len(M)):
            sous_liste.append(M[j][i])
        L.append(sous_liste)
    return L   
    
def genmatrix_inv(n):
  m = gentrianginf_inv(n,10)
  b = gentrianginf_inv(n, 10)
  b_t = transpose(b)
  print_matrice(m)
  print_matrice(b_t)
  C = []
  for i in range(len(m)):
    L = []
    for j in range(len(m)):
      res = 0
      for k in range(len(m)):
        res += m[i][k]*b_t[k][j] 
      L.append(res)
    C.append(L)
  return C
  
 def matvec(M, V):
  L = []
  for i in range(len(M)):
    res = 0
    for j in range(len(V)):
      res += M[i][j]*V[j]
    L.append(res)
  return L
 
 def circmultvec(V, Y):
  L = []
  for i in range(len(V)):
    res = 0
    for j in range(len(V)):
      res += V[j]*Y[j]
    V = [V[-1]] + V[:len(V)-1]
    L.append(res)
  return L
  
 def circmultmat(A,B):
  R = []
  B.reverse()
  B = [B[-1]] + B[:-1]
  for i in range(len(A)):
    L = []
    for j in range(len(B)):
      res = 0
      for k in range(len(B)):
        res += A[k]*B[k]
      B = [B[-1]]+ B[:-1]
      L.append(res)
    R.append(L)
    A = [A[-1]] + A[:-1]
  return R
  
def prod_perm2(M, V):
  L = []
  for i in range(len(M)):
    num = M[i]
    j = 0
    while num != 0 and (num & 1) == 0 :
      j += 1
      num = num >> 1 
    L.append(V[-j-1])
  return L
  
def permute_from_list(L, V):
  liste = []
  for i in range(len(L)):
    x = L[i]
    liste.append(V[x])
  return liste
  
 
def is_triangsup(M):
  if len(M) != len(M[0]):
    return False 
  for i in range(len(M)):
    for j in range(i):
      if M[i][j] == 0:
        pass
      else :
        return False
  return True 
  
 def is_diag_dom(M):
  diag = 0
  boolean = True
  i = 0
  while i>= 1
  return res 
print(puissance(2,5,10),(2**5)%10)


