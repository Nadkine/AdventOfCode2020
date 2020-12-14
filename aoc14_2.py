codes = []

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

def getBits(the_bin,mask):
    results = [""]
    new_number = ''
    counter = 0
    for n,maskn in zip(reversed(the_bin),reversed(mask)): 
        counter += 1
        results_copy = results.copy()
        if maskn == "0":
            for result in results_copy:
                new_number = str(n) + result
                results.append(new_number)
        if maskn == "1":
            for result in results_copy:
                new_number = "1" + result
                results.append(new_number)
        if maskn == "X":
            for result in results_copy:
                new_number1 = "0" + result
                new_number2 = "1" + result
                results.append(new_number1)
                results.append(new_number2)
        results_copy = [i for i in results if counter == len(i) ]
        results = results_copy
    return results 

codes = codes[1:]
dicto = {}
for code in codes:
    mask = code[0]
    for instr in code[1:]:
        id = int(instr[0])
        getal = int(instr[1])
        the_bin = str(bin(id))[2:].zfill(36)
        results = getBits(the_bin,mask)
        for result in results:
            dicto[int(result,base=2)] = getal
print(sum(list(dicto.values())))

    

          



