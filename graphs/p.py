G = [
    [1, 6, 7],
    [0, 2, 4, 5, 6],
    [1],
    [5, 6, 8],
    [1],
    [1, 3, 6],
    [0, 1, 3, 5, 7],
    [0, 6, 8],
    [3, 7]
]

H = [
    [1, 2, 4],
    [3, 5],
    [6],
    [],
    [5],
    [],
    [],
]

def visiter(k):
    # action à effectuer dans le parcours lors de la visite du sommet k
    print(k, end=' ') # Pour avoir les sommets en numéro
## print(chr(ord('A')+k), end=' ') # Pour avoir les sommets en lettres


def sommet_valid(n):
    v=input('Saisir le sommet d entrée ')
    
    while (len(v)!=1 or (ord(v)< ord('0') or ord(v)>=ord('0')+n) ):
        v=input('Saisir le sommet d entrée ')
        
    return(int(v))

def parcours(graphe):
    n = len(graphe)

## depart=int(input("Sommet de départ ?"))
depart=sommet_valid(n) # saisie du sommet de départ
depuis = []
depuis.append(depart) # j'empile le sommet que j'explore
dejavu = [False for k in range(n)] # Initialisation de la table des 'visités'

while len(depuis)!=0:
    k = depuis.pop() # Pour une exploration en profondeur, on récupére le dernier sommet de la liste des sommets accessibles
    # ATTENTION depuis.pop(0) explore en largeur de droite à gauche

    if dejavu[k]:
        continue

dejavu[k] = True
visiter(k)

for s in graphe[k]:
    depuis.append(s)
