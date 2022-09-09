# === Ex7 ===

def li_cat(n, l = []):
    if n in (0, 1): return set(l + [1])
    n -= 1
    
    li = [sum(li_cat(i)) * sum(li_cat(n - i)) for i in range(n)]
        
    return li_cat(n, l + li)

# print(li_cat(7))

# === Ex9 ===

def recherche_dico(l: list, x: int) -> bool:
    if not len(l): return False
    if x == l[0]: return True
    
    med = len(l) // 2
    
    if x == l[med]: return True
    elif x < l[med]: return recherche_dico(l[:med], x)
    elif x > l[med]: return recherche_dico(l[med:], x)

# print(recherche_dico([0, 1, 2, 4, 18], 2))