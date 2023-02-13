def multiplication(b, c, f):
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

def sous_groupe_gen(b,f):
    L = []
    i = 0
    c = 1
    for i in range(f):
        L.append(multiplication(b,c,f))
    return L

print(sous_groupe_gen(2,39))











Un polynôme de degré n sur le corps F2 comporte n+1 coefficients qui valent soit 0, soit 1. Ainsi on peut coder un tel polynôme par un entier dont la décomposition en base 2 représente la liste des coefficients du polynôme.

Exemple : l'entier 39 représente le polynôme x5+x2+x+1. En effet l'entier 39 en base 2 se représente par 100111, le coefficient de plus haut degré est le bit de poids fort de l'entier et celui du terme constant est le bit de poids faible.

Ecrire la fonction sous_groupe_gen(b,f) où

f est un entier représentant un polynôme de degré m irréductible sur F2,
b est un entier dont la représentation en base 2  donne la décomposition dans la base {αm−1,αm−2,…,α,1} d'un élément u∈F2m, α étant une racine de f.
Cette fonction doit renvoyer  la liste des entiers représentant les éléments du sous-groupe de F∗2m généré par l'élément u.

IMPORTANT : votre fonction sera exécutée dans un environnement où la fonction multiplication(b,c,f) existe, vous pouvez donc y faire appel dans le corps de votre fonction, il est inutile de la redéfinir.
Cette fonction s'écrit sans l'instruction if.

Réponse :(régime de pénalités : 0, 0, 5, 10, 15, ... %)


Déduire de l'exercice précédente la fonction ordre(b,f) où :

f est un entier représentant un polynôme de degré m irréductible sur F2,
b est un entier dont la représentation en base 2  donne la décomposition dans la base {αm−1,αm−2,…,α,1} d'un élément u∈F2m, α étant une racine de f.
Cette fonction doit renvoyer  l'ordre de l'élément u dans F∗2m.

IMPORTANT : votre fonction sera exécutée dans un environnement où la fonction sous_groupe_gen(b,f) existe, vous pouvez donc y faire appel dans le corps de votre fonction, il est inutile de la redéfinir.
Cette fonction s'écrit en une seule ligne.

Réponse :(régime de pénalités : 0, 0, 5, 10, 15, ... %)



Soit P(x) un polynôme primitif  sur F2 de degré m utilisé pour construire le corps (F2m,+,×). Soit α la racine de ce polynôme, alors on sait que α est un générateur de (F2m)∗ et donc

F2m={0,1,α,α2,α3,…,α2m−2}

Ainsi tout élément u≠0 de F2m est de la forme αi.

Soit u≠0 un élément de F2m, le symétrique pour la loi × de u est l'élément v tel que le produit de u par v donne 1 dans le corps  F2m.

Ecrire la fonction symetrique_mul(x,P) où x est un entier représentant un élément u≠0 du corps F2m construit à partir du polynôme P. Cette fonction doit renvoyer l'entier z qui représente le symétrique pour la loi × de u dans F2m.

Le polynôme P sera codé par un entier dont la décomposition en base 2 représente la liste des coefficients du polynôme.


Par exemple, le polynôme P(x)=x3+x2+1 (représenté par l'entier 13) est primitif sur F2. Il permet de construire le corps (F23,+,×). Dans ce corps α2 est représenté par l'entier x=4, et son symétrique multiplicatif est α+1, représenté par l'entier z=3. En effet

α2×(α+1)=α3+α2=1 car α3=α2+1.

Ainsi symetrique_mul(4,13) doit renvoyer 3.
Cette fonction s'écrit sans aucune boucle. Votre fonction sera évaluée dans un environnement où vous avez accès à 2 listes :

la liste log_table : pour un entier x représentant un élément u de F2m, log_table[x] contient l'entier i tel que u=αi,
la liste alpha_table : pour un entier i compris entre 0 et 2m−1, alpha_table[i] contient l'entier z qui représente l'élément αi de F2m.
Vous pouvez utiliser l'instruction bin qui renvoie la décomposition en base 2 d'un entier.

Réponse :(régime de pénalités : 0, 0, 5, 10, 15, ... %)

Un polynôme de degré n sur le corps F2 comporte n+1 coefficients qui valent soit 0, soit 1. Ainsi on peut coder un tel polynôme par un entier dont la décomposition en base 2 représente la liste des coefficients du polynôme.

Exemple : l'entier 39 représente le polynôme x5+x2+x+1. En effet l'entier 39 en base 2 se représente par 100111, le coefficient de plus haut degré est le bit de poids fort de l'entier et celui du terme constant est le bit de poids faible.

Ecrire la fonction is_sym_mul(b,c,f) où

f est un entier représentant un polynôme de degré m irréductible sur F2,
b est un entier dont la représentation en base 2  donne la décomposition dans la base {αm−1,αm−2,…,α,1} d'un élément u∈F2m, α étant une racine de f.
c est un entier dont la représentation en base 2  donne la décomposition dans la base {αm−1,αm−2,…,α,1} d'un élément v∈F2m.
Cette fonction doit renvoyer :

True, si l'élément v∈Fm2 représenté par  c est le symétrique pour la loi × de l'élément u∈Fm2 représenté par  b.
 False, sinon.
IMPORTANT : votre fonction sera exécutée dans un environnement où la fonction multiplication(b,c,f) existe, vous pouvez donc y faire appel dans le corps de votre fonction, il est inutile de la redéfinir.

Cette fonction s'écrit sans aucune boucle et sans l'instruction if.

Réponse :(régime de pénalités : 0, 0, 5, 10, 15, ... %)



Soit P(x) un polynôme primitif  sur F2 de degré m utilisé pour construire le corps (F2m,+,×). Soit α la racine de ce polynôme, alors on sait que α est un générateur de (F2m)∗ et donc

F2m={0,1,α,α2,α3,…,α2m−2}

Ainsi tout élément u≠0 de F2m est de la forme αi.

Un polynôme de degré n sur le corps F2 comporte n+1 coefficients qui valent soit 0, soit 1. Ainsi on peut coder un tel polynôme par un entier dont la décomposition en base 2 représente la liste des coefficients du polynôme.
Exemple : l'entier 39 représente le polynôme x5+x2+x+1. En effet l'entier 39 en base 2 se représente par 100111, le coefficient de plus haut degré est le bit de poids fort de l'entier et celui du terme constant est le bit de poids faible.

Ecrire la fonction is_sym_mul(b,c,f) où

f est un entier représentant un polynôme de degré m primitif sur F2,
b est un entier dont la représentation en base 2  donne la décomposition dans la base {αm−1,αm−2,…,α,1} d'un élément u∈F2m, α étant une racine de f.
c est un entier dont la représentation en base 2  donne la décomposition dans la base {αm−1,αm−2,…,α,1} d'un élément v∈F2m.
Cette fonction doit renvoyer :

True, si l'élément v∈Fm2 représenté par  c est le symétrique pour la loi × de l'élément u∈Fm2 représenté par  b.
 False, sinon.
IMPORTANT : votre fonction sera exécutée dans un environnement où vous avez accès à 2 listes :

la liste log_table : pour un entier x représentant un élément u de F2m, log_table[x] contient l'entier i tel que u=αi,
la liste alpha_table : pour un entier i compris entre 0 et 2m−1, alpha_table[i] contient l'entier z qui représente l'élément αi de F2m.

Cette fonction s'écrit sans aucune boucle et sans l'instruction if. Vous pouvez utiliser l'instruction bin qui renvoie la décomposition en base 2 d'un entier.

Réponse :(régime de pénalités : 0, 0, 5, 10, 15, ... %)
