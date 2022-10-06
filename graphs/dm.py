#!/usr/bin/python3

creer_pile = lambda: []
hauteur = lambda l: len(l)
sommet = lambda l: l[-1]
est_vide = lambda l: not len(l)
empiler = lambda l, x: l.insert(0, x)
depiler = lambda l: l.pop()
defiler = lambda l: l.pop(0)
enfiler = lambda l, i: l.append(i)

def dec_to_bin(n: int) -> int:
    
    pile = creer_pile()
    file = creer_pile()
    
    while n != 0:
        r, n = n % 2, n // 2
        enfiler(pile, str(r))
    
    while not est_vide(pile):
        enfiler(file, depiler(pile))
    
    return int(''.join(file))

# print(dec_to_bin(77))

def base_converter(n: int, b: int) -> int:
    
    pile = creer_pile()
    
    while n:
        r = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[n % b]
        n //= b
        empiler(pile, str(r))
    
    return ''.join(pile)

# print(base_converter(255, 16))
