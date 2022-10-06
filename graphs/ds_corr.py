#!/usr/bin/python3

bin_to_dec = lambda x: int(x[-1]) + 2 * bin_to_dec(x[:-1]) if len(x) else 0
dec_to_bin = lambda x: str(dec_to_bin(x // 2)) + str(x % 2) if x != 0 else ''

# print(dec_to_bin(bin_to_dec('1001101')))

def pal(s):
    if s == '': return True
    return pal(s[1:-1]) if s[0] == s[-1] else False

print(pal('ressasser'))