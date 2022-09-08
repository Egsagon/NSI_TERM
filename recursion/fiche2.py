# === Ex1 ===

def puissance(x, n) -> int: return x * (x ** (n - 1))

# print(puissance(3, 2))

def puissance2(x, n) -> int:
    if x <= 0 or n <= 0: return 1
    
    if n % 2 == 0: return puissance2(x, n / 2) ** 2
    else: return x * puissance2(x, (n - 1) / 2) ** 2

# print(puissance2(4, 4))

# === Ex2 ===

def binomial(n, p) -> int:
    if p > n or p < 0: return 0
    if p == 0: return 1
    
    return int(n / p * binomial(n - 1, p - 1))

# print(binomial(10, 3))

# === Ex3 ===

def maximum(li, i = 0, m = 0) -> int:
    if i > len(li) - 1: return m
    
    if li[i] > m: m = li[i]
    i += 1
    
    return maximum(li, i, m)

# print(maximum([9, 2, 3, 4, 5]))

# === Ex4 ===

def miroir(string, rev = '') -> str:
    if len(string) == 0: return rev
    
    string, el = string[1:], string[0]
    return miroir(string, f'{el}{rev}')

print(miroir('abcde'))
