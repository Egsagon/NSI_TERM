#!/usr/bin/python3

from copy import copy

creer_pile = lambda: []
hauteur = lambda l: len(l)
sommet = lambda l: l[-1]
est_vide = lambda l: not len(l)
empiler = lambda l, x: l.append(x)
depiler = lambda l: l.pop()
defiler = lambda l: l.pop(0)
enfiler = lambda l, i: l.append(i)

f = ['rouge', 'vert', 'jaune', 'rouge', 'jaune']

def former_pile(f: list):
    
    p = creer_pile()
    while not est_vide(f): empiler(p, defiler(f))
    return p

# print(former_pile(f))

def nb_elements(f: list, el: str):
    # return len([1 for i in f if i == el])
    
    f = copy(f)
    return len([1 for i in range(hauteur(f))
                if defiler(f) == el])

print(nb_elements(f, 'rouge'))

def verifier_contenu(f: list, *nbs: list[int]):
    
    return nb_elements(f, 'rouge') <= nbs[0] and \
           nb_elements(f, 'jaune') <= nbs[1] and \
           nb_elements(f, 'vert' ) <= nbs[2]
           
# print(verifier_contenu(f, 2, 2, 1))
