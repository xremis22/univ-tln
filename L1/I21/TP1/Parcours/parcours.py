#
# FIchier à compléter: parcours.py
#
# Chaque fonction retourne la liste des paires d'indices correspondant
# au parcours nommé.
#

def parcours_ligne(n):
    """Retourne la liste des indices (colonne,ligne) (!!attention ici
    ligne et colonne sont inversées!!)  des cases correspondant à un
    parcours tableau de taille n x n en ligne.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 1,2,3,4,5,6,7,8,9 et la 
    fonction retournera la liste d'indices [(0,0),(1,0),(2,0),(0,1) ...]

    """

    return [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9)]

    
def parcours_colonne(n):
    """Retourne la liste des indices (colonne,ligne) (!!attention ici
    ligne et colonne sont inversées!!)  des cases correspondant à un
    parcours de tableau de taille n x n en colonne.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 1,4,7,2,5,8,3,6,9 et la 
    fonction retournera la liste d'indices [(0,0),(0,1),(0,2),(1,0) ...]

    """
    return []
    
def parcours_diagonal(n):
    """Retourne la liste des indices (colonne,ligne) (!!attention ici
    ligne et colonne sont inversées!!)  des cases correspondant à un
    parcours de tableau de taille n x n en diagonale.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 3,2,6,1,5,9,4,8,7 et la 
    fonction retournera la liste d'indices [(2,0),(1,0),(2,1),(0,0) ...]

    """
    return []
    
def parcours_antidiagonal(n):
    """Retourne la liste des indices (colonne,ligne) (!!attention ici
    ligne et colonne sont inversées!!)  des cases correspondant à un
    parcours de tableau de taille n x n en anti-diagonale.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 9,6,8,3,5,7,2,4,1 et la 
    fonction retournera la liste d'indices [(2,2),(2,1),(1,2),(2,0) ...]

    """
    return []
    
def parcours_serpentin(n):
    """Retourne la liste des indices (colonne,ligne) (!!attention ici
    ligne et colonne sont inversées!!)  des cases correspondant à un
    parcours de tableau de taille n x n en serpentin.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 1,2,3,6,9,8,7,4,5 et la 
    fonction retournera la liste d'indices [(0,0),(1,0),(2,0),(2,1) ...]

    """
    return []

def parcours_sinusoidal(n): 
    """Retourne la liste des indices (ligne,
    colonne) des cases correspondant a un parcours sinusoidal d'un
    tableau de taille n x n.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 1,4,7,8,5,2,3,6,9 et la 
    fonction retournera la liste d'indices :
    [(0,0),(1,0),(2,0),(2,1),(2,2) ...]

    """
    return []

def parcours_zigzag(n):
    """Retourne la liste des indices (ligne,
    colonne) des cases correspondant a un parcours sinusoidal d'un
    tableau de taille n x n.

    Ex: pour T = [ [1,2,3],
                   [4,5,6],
                   [7,8,9] ]
    le parcours correspond aux cases 1,2,3,6,5,4,7,8,9 et la 
    fonction retournera la liste d'indices :
    [(0,0),(0,1),(0,2),(1,2),(1,1) ...]

    """
    return []


print(parcours_ligne(10))
