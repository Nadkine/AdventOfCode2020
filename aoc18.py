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
    subsumstarted = 0
    last_index_plus = 0
    for i,letter in enumerate(row_copy):
        i += inserted
        if letter == "+":
            last_index_plus = i
            if row[i-1] != ")" and not subsumstarted:
                row.insert(i-1, "(")
                inserted += 1
                last_index_plus += 1
                subsumstarted += 1
        if letter == "*":
            if row[i-1] == ")":
                row.insert(i-1, ")")
                row.insert(0,"(")
                inserted += 1
                subsumstarted -= 1
            if subsumstarted > 0 and row[i-2] != "(":
                row.insert(i, ")")
                inserted += 1
                subsumstarted -= 1 
        if letter == ")":
            if subsumstarted > 0:
                row.insert(i, ")")
                inserted += 1
                subsumstarted -= 1
    while subsumstarted > 0:
         row.append(")")
         subsumstarted -= 1
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


