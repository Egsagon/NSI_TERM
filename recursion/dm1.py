#!/usr/bin/python3

# === Ex7 ===

def li_cat(n):
    if n == 0: return [1]
    
    n -= 1
    l = li_cat(n)
    
    return l + [sum([l[i] * l[n - i] for i in range(n + 1)])]

# print(li_cat(7))
# TODO: include l as an argument

# === Ex9 ===

def recherche_dico(l: list, x: int) -> bool:
    if not len(l): return False
    if x == l[0]: return True
    
    med = len(l) // 2
    
    if x == l[med]: return True
    elif x < l[med]: return recherche_dico(l[:med], x)
    elif x > l[med]: return recherche_dico(l[med:], x)

# print(recherche_dico([0, 1, 2, 4, 18], 2))