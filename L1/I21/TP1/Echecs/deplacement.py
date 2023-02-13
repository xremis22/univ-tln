#
# Fichier à compléter: deplacement.py
#
# Chaque fonction doit renvoyer la liste des indices (col,lig) des
# cases sur lesquelles la pièce en question peut aller.
#

def cases_fou(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionné sur la case (col, lig)

    Ex: fou en (2,3)
    - - - - - - - - - -
    |           x     |
    | x       x       |
    |   x   x         |
    |     F           |
    |   x   x         |
    | x       x       |
    |           x     |
    |             x   |
    - - - - - - - - - -

    """
    L=[]
    c=col+1
    l=lig-1
    while c < 8 and l >= 0:
        L+=[(c,l)]
        c+=1
        l-=1
    c=col-1
    l=lig+1
    while c >= 0 and l < 8:
        L+=[(c,l)]
        c-=1
        l+=1
    c=col+1
    l=lig+1
    while c < 8 and l < 8:
        L+=[(c,l)]
        c+=1
        l+=1
    c=col-1
    l=lig-1
    while c >= 0 and l >= 0:
        L+=[(c,l)]
        c-=1
        l-=1
    return L


def cases_tour(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer une tour positionnée sur la case (col, lig)

    Ex: tour en (5,3)
    - - - - - - - - - -
    |           x     |
    |           x     |
    |           x     |
    | x x x x x T x x |
    |           x     |
    |           x     |
    |           x     |
    |           x     |
    - - - - - - - - - -

    """
    L=[]
    l=lig-1
    c=col
    while l >= 0:
        L+=[(c,l)]
        l-=1
    l=lig+1
    c=col
    while l < 8:
        L+=[(c,l)]
        l+=1
    c=col-1
    l=lig
    while c >= 0:
        L+=[(c,l)]
        c-=1
    c=col+1
    l=lig
    while c < 8:
        L+=[(c,l)]
        c+=1
    return L

def cases_reine(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionnée sur la case (col, lig)

    Ex: dame en (6,1)
    - - - - - - - - - -
    |           x x x |
    | x x x x x x D x |
    |           x x x |
    |         x   x   |
    |       x     x   |
    |     x       x   |
    |   x         x   |
    | x           x   |
    - - - - - - - - - -

    """
    L=[]
    l=lig-1
    c=col
    while l >= 0:
        L+=[(c,l)]
        l-=1
    l=lig+1
    c=col
    while l < 8:
        L+=[(c,l)]
        l+=1
    c=col-1
    l=lig
    while c >= 0:
        L+=[(c,l)]
        c-=1
    c=col+1
    l=lig
    while c < 8:
        L+=[(c,l)]
        c+=1

    c=col+1
    l=lig-1
    while c < 8 and l >= 0:
        L+=[(c,l)]
        c+=1
        l-=1
    c=col-1
    l=lig+1
    while c >= 0 and l < 8:
        L+=[(c,l)]
        c-=1
        l+=1
    c=col+1
    l=lig+1
    while c < 8 and l < 8:
        L+=[(c,l)]
        c+=1
        l+=1
    c=col-1
    l=lig-1
    while c >= 0 and l >= 0:
        L+=[(c,l)]
        c-=1
        l-=1

    return L

def cases_roi(col,lig):
   """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un roi positionné sur la case (col, lig)

    Ex: Roi en (4,5)
    - - - - - - - - - -
    |                 |
    |                 |
    |                 |
    |                 |
    |      x x x      |
    |      x R x      |
    |      x x x      |
    |                 |
    - - - - - - - - - -

   """

#Prof
   case=[]
   c=col
   l=lig
   for i in (-1,0,+1):
      for j in (-1,0,+1):
         if (0 <= c + i < 8) and (0 <= l + j < 8) and not (i==j==0):
            case+=[(c+i,l+j)]
   return case



def cases_cavalier(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionné sur la case (col, lig)

    Ex: cavalier en (3,3)
    - - - - - - - - - -
    |                 |
    |     x   x       |
    |   x       x     |
    |       C         |
    |   x       x     |
    |     x   x       |
    |                 |
    |                 |
    - - - - - - - - - -

    """
    return []

def cases_pion(col,lig):
    """Retourne la liste des indices (col,lig) des cases où peut se
    déplacer un fou positionné sur la case (col, lig)

    Ex: pions en (1,6) et (5,3)
    - - - - - - - - - -
    |                 |
    |                 |
    |           x     |
    |           P     |
    |   x             |
    |   x             |
    |   P             |
    |                 |
    - - - - - - - - - -

    """
    return []
