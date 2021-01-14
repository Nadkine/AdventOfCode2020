rows = []

# (8*2)+4+3+7*2
# (8*2)+(4+3+7)*2
with open('data18.txt','r') as f:
   for line in f.read().splitlines():
       rows.append([letter for letter in line])

all_sums = []
for row in rows:
    print("--------")
    inserted = 0
    row = [i for i in row if i != " "]

    print("".join(row))
    #row.insert(0,"(")
    row_copy = row.copy()
    substart = {0:True}     
    substartindex = 0
    last_plus_index = 0
    inserted = 0
    row_copy.insert(0,"(")
    for i,letter in enumerate(row_copy):
        i += inserted
        if letter == "+":
            row.insert(i-1,"(")
            inserted += 1
            substartindex += 1
            last_plus_index = i 
            substart[substartindex] = True          
        if letter == ")":
            if substart[substartindex]:
                row.insert(i,")")
                inserted += 1
                substart[substartindex] = False
                substartindex -= 1 
        if letter == "(":
            substartindex += 1
            substart[substartindex] = True
        if letter == "*":
            if substart[substartindex]:
                row.insert(last_plus_index+1,")")
                substart[substartindex] = False
                substartindex -= 1
    print(substart)
    print(substartindex)
    while substartindex in substart:
        print(substartindex)
        row.append(")")
        substartindex -= 1

    print("".join(row))
    subsum = {0:["+",0]}     
    subsum_index = 0
    operator = '+'
    for letter in row:
        if letter == "(":
            subsum_index += 1
            subsum[subsum_index] = [operator,0]
            operator = "+"
        elif letter == ")":
            thesum = subsum[subsum_index][1]
            suboperation = subsum[subsum_index][0]
            #print(thesum,suboperation)
            subsum_index -= 1
            #print(subsum[subsum_index][1])
            if suboperation == "+":
                subsum[subsum_index][1] += thesum
            if suboperation == "*":
                subsum[subsum_index][1] *= thesum
        elif letter == "+":
            operator = "+"
        elif letter == "*":
            operator = "*"
        else:
            if operator == "+":
                subsum[subsum_index][1] += int(letter)
            if operator == "*":
                subsum[subsum_index][1] *= int(letter)
    all_sums.append(subsum[subsum_index][1])
    print(subsum[subsum_index][1])
print(sum(all_sums))


