def is_sym_add(x,y,n) :
    k = n - x
    return k == y

#print(is_sym_add(12,5,17))

def is_sym_mult(x,y,n) :
    k = (x*y)%n
    return k == 1

#print(is_sym_mult(29,8,33))

def is_sym_add(x,y) :
    k = [abs(y[0]),y[1]]
    print(k)
    return x == k
print(is_sym_add([6,18],[-9,27]))

def pgcd(a,b):
    c=0
    while b>a :
        c=a
        a=b
        b=c
    if b==0:
        return a
    else :
        reste=a%b
        return pgcd(b,reste)

def phi(n) :
    if

def is_of_order(a,t,n) :









#

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


def is_sym_add(x, y, n):
    return((x + y)%n == 0)

def is_sym_mult(x, y, n):
    return((x*y)%n==1)

def is_sym_add(x, y):
    return(x[0]*y[1]+y[0]*x[1])

def is_sym_mult(x, y):
    return((x[0]*y[0])==(x[1]*y[1]))

def is_of_order(a, t, n):
    return(t==(n//pgcd(a, n)))

def is_of_order_mult(a, t, n):
    x = ((pow(a, t, n)==1) and (a!=1))
    i = 2
    while(x and (i*i <= t)):
        if(t%j)==0 :
            x = ((pow(a, i, n)!=1) and pow(a, t//i, n) != 1):
        i += 1
    return(x or ((a==1) and (t==1))
    
