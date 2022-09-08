# === Ex1 ===

def length(string, n = 0) -> int:
    if not string: return n
    
    return length(string[:-1], n + 1)

# print(length('abcdejjsfjdf'))

# === Ex2 ===

def somme(li, s = 0) -> int:
    if len(li) == 0: return s
    
    li, el = li, li.pop(-1)
    
    return somme(li, s + el)

# print(somme([1, 2, 3, 5]))

# === Ex3 ===

def binaire(n, s = '') -> str:
    if n <= 0: return s
    
    return binaire(n // 2, s + str(n % 2))

# print(binaire(5))

# === Ex5 ===

def suite(n) -> float:
    if n < 2: return 1
    
    return 3 * suite(n - 1) + suite(n - 2)

# print(suite(5))
