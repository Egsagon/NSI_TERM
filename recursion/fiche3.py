#!/usr/bin/python3

def low(string: str) -> str:
    r = ''

    for char in string:
        he = hex(ord(char)).replace('0x', '')
        r += chr(int(he, 16) + int('20', 16)) if 65 <= int(he, 16) <= 90 else char
        
    return r

# print(low('ABCEFGGG[]dsqdsqdA'))

def pal(string: str) -> bool:
    
    # string = string.lower()
    string = low(string)
    for c in ' \'-': string = string.replace(c, '')
    
    if string == '': return True
    if string[-1] == string[0]: return pal(string[1:-1])
    
    return False

# print(pal("Engage le jeu que je le gagne"))
