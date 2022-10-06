#!/usr/bin/python3

G = {
    'A': [('B', 11.2),
          ('C', 10.9),
          ('D',  8.8)],
    'B': [('A', 11.2),
          ('C',  7.8),
          ('G', 12.4)],
    'C': [('A', 10.9),
          ('B',  7.8),
          ('D',  7.9),
          ('E',   12),
          ('G',  9.3)],
    'D': [('A',  8.8),
          ('C',  7.9),
          ('E',  9.9),
          ('F',  8.5)],
    'E': [('C',   12),
          ('D',  9.9),
          ('F',  7.8),
          ('G', 11.4),
          ('H',   10)],
    'F': [('D',  8.5),
          ('E',  7.8),
          ('H',    8)],
    'G': [('B', 12.4),
          ('C',  9.3),
          ('E', 11.4),
          ('H',    9)],
    'H': [('G',    9),
          ('E',   10),
          ('F',    8)]
}

start = 'A'
end = 'H'

grill = [False for _ in G.keys()]
table = [[['', 0] for _ in G.keys()]]

