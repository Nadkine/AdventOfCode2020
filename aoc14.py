codes = []
from astropy.nddata import bitmask
import numpy as np
#mem[41248] = 4595332
with open('data14.txt','r') as f:
    batch = []
    for line in f.read().splitlines():
        if line[:4] == "mask":
           codes.append(batch)
           batch = [line[7:]]
        else:
            index = line.index("=")
            batch.append([int(line[4:index-2]),int(line[index+1:])])
    codes.append(batch)
codes = codes[1:]
dicto = {}
for code in codes:
    mask = code[0]
    for instr in code[1:]:
        id = int(instr[0])
        number = int(instr[1])
        the_bin = str(bin(number))[2:].zfill(36)
        new_number = ''
        for n,maskn in zip(reversed(the_bin),reversed(mask)):
            if maskn == "X":
                i = str(n)
            else:
                i = str(maskn)
            new_number = i + new_number
        dicto[id] = int(new_number,base=2)
print(sum(list(dicto.values())))

        

          



