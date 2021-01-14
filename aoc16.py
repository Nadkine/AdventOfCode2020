import numpy as np

data = {}
data['nearby_tickets']= []
my_tickets = False
nearby_tickets = False
with open('data16.txt','r') as f:
    for index,line in enumerate(f.read().splitlines()):
        if index < 20:  
            indexcolon = line.index(":")
            indexor = line.index(" or ")
            data[line[:indexcolon+1]] = [line[indexcolon+2:indexor],line[indexor+4:]]
        elif index > 21 and index < 23:
            data['my_ticket'] = line.split(',')
        else:
            data['nearby_tickets'].append([i for i in line.split(',')])
    data['nearby_tickets'] = data['nearby_tickets'][4:]
possible_values = set()

for i in list(data.values())[1:-1]:
    for k in i:
        number1 = int(k[:k.index("-")])
        number2 = int(k[k.index("-")+1:])
        for j in range(number1,number2+1):
            possible_values.add(j)

error = 0
for ticket in data['nearby_tickets'][4:]:
    for item in ticket:
        if int(item) not in possible_values:
            data['nearby_tickets'].remove(ticket)

all_possibilities = []
for n in range(len(data['nearby_tickets'][0])):
    print(n)
    possibilities = []
    for i in range(len(data['nearby_tickets'])):
        possible = True
        for j in list(data.values())[1:-1]:
            number1 = int(j[0][:j[0].index("-")])
            number2 = int(j[0][j[0].index("-")+1:])
            number3 = int(j[1][:j[1].index("-")])
            number4 = int(j[1][j[1].index("-")+1:])
            #print(number1,number2,number3,number4)
            if not ((int(data['nearby_tickets'][i][n]) >= number1 and int(data['nearby_tickets'][i][n]) <= number2) or \
                (int(data['nearby_tickets'][i][n]) >= number3 and int(data['nearby_tickets'][i][n]) <= number4)) :
                possible = False

        possibilities.append(possible)
    all_possibilities.append(possibilities)
board = np.array(all_possibilities,dtype=np.bool)
print(board.shape)

for i in range(21):
    possible = True
    for n in range (192):
        for j in board[i,]:
            if not j:
                possible = False
        print(possible)
        if possible:
            print(n,i)


        
   



