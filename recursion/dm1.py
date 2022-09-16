#!/usr/bin/python3

# === Ex7 === #

PAR = ('(', ')')

def cat(n: int) -> list:
    if not n: return [1]
    
    n -= 1
    li = cat(n)
    return li + [sum([li[i] * li[n - i] for i in range(n + 1)])]

# print(cat(7))

'''
def par(n: int, li = []) -> list:
    if not n: return ['']
    if n == 1: return [''.join(PAR)]
    
    return [f'{PAR[0]}{b}{PAR[1]}{a}'
            for i in range(n)
                for b in par(i)
                    for a in par(n - 1 - i)]
'''

def par(n: int, li = []) -> list:
    if not n: return ['']
    if n == 1: return [''.join(PAR)]
    
    return [PAR[0] + str(b) + PAR[1] + str(a) for i in range(n) for b in par(i) for a in par(n - 1 - i)]

# print(par(3))

# === Ex9 === #

def rec(l: list, x: int) -> bool:
    if not len(l) or x < l[0] or x > l[-1]: return False
    if x == l[0]: return True
    
    m = len(l) // 2
    
    if x == l[m]: return True
    elif x < l[m]: return rec(l[:m], x)
    elif x > l[m]: return rec(l[m:], x)

# print(rec(list(range(100)), 10))
# print(rec([1, 2, 3], 4))
