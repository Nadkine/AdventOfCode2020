board = []
board_copy = []
with open('data11.txt','r') as f:
    for line in f.readlines():
        row = []
        for seat in line:
            if seat != '\n':
                row.append(seat)
        board.append(row)
different = True
counter = 0


def getSeats(row_i, seat_i,board,row_counter,seat_counter):
    k = 0
    l = 0
    while True:
        k += row_counter
        l += seat_counter
        if row_i+k < 0 or row_i+k > len(board)-1:
            return 1
        elif seat_i+l < 0 or seat_i+l > len(board[row_i])-1:
            return 1
        elif board[row_i + k][seat_i + l] == ".":
            pass
        elif board[row_i + k][seat_i + l] == "L":
            return 1
        elif board[row_i + k][seat_i + l] == "#":
            return 0
        
        

while different:
    counter += 1
    print(counter)
    #get comparisonboard
    board_copy = []
    for row in board:
        board_copy.append(row.copy())

    for row_i,row in enumerate(board):
        for seat_i,seat in enumerate(row):
            available = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if not(x==0 and y ==0):
                        available += getSeats(row_i,seat_i,board_copy,x,y)            
            if available == 8 and seat == "L":
                board[row_i][seat_i] = "#"
            if available < 4 and seat == "#": 
                board[row_i][seat_i] = "L"   
    #check if the same (not clean) 
    board_count = 0
    board_copy_count = 0
    for row in board:
        board_count += row.count('#')
    for row in board_copy:
        board_copy_count += row.count('#')
    print(board_count)
    if board_copy_count == board_count:
        different = False
print("FINISHED")




                