obj = [
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

def prof(obj: list, start: int,
         sort: callable = lambda l: l) -> list:

    done = [False for _ in range(len(obj))]
    path = [start]
    pile = [start]

    while not all(done):
        
        done[pile[-1]] = True
        nbs = obj[pile[-1]]
        
        nbs = sort(nbs)
        
        b = 0
        for nb in nbs:
            if done[nb]: b += 1
            
            else:
                path += [nb]
                pile += [nb]
                
                done[nb] = True
                break
        
        if b == len(nbs): s = pile.pop(-1)

    return path

print(prof(obj, 0))
