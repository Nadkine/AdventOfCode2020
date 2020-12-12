instructions = []
with open('data12.txt','r') as f:
    for line in f.read().splitlines():
        instructions.append(line)

compass = [[1,0],[0,-1],[-1,0],[0,1]]
pos = [0,0]
face = [1,0]
way = [10,1]

for instr in instructions:
    dir = instr[:1]
    amount = int(instr[1:])
    if dir == "N":
        way[1] += amount
    if dir == "E":
        way[0] += amount
    if dir == "S":
        way[1] -= amount
    if dir == "W":
        way[0] -= amount
    if dir == "L" or dir == "R":
        amount = int(amount/90)
        loc_i = compass.index(face)
        if dir == "L":
            loc_i = (loc_i - amount) % 4
        else:
            loc_i = (loc_i + amount) % 4
        face = compass[loc_i]
        if amount % 2 == 0:
            way[0] *= -1
            way[1] *= -1
        elif (amount == 3 and dir == "L") or (amount == 1 and dir == "R"):
            way = [way[1],-way[0]]
        else:
            way = [-way[1],way[0]]
    if dir == "F":
        pos[0] += way[0] * amount
        pos[1] += way[1] * amount

print(abs(pos[0]) + abs(pos[1]))