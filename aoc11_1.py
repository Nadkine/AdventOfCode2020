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
        if row_i-k == 0:
            return 1
        elif board[row_i + k][seat_i -1] == ".":
            pass:
        elif board[row_i + k][seat_i-1] == "L":
            return 1
        elif board[row_i + k][seat_i-1] == "#":
            return 0
        

while different:
    counter += 1
    print(counter)
    board_copy = []
    for row in board:
        board_copy.append(row.copy())

    for row_i,row in enumerate(board):
        for seat_i,seat in enumerate(row):
            available = 0
            if (row_i == 0                                             or board_copy[row_i - 1][seat_i] != '#'):   
                available += getSeats(row_i,seat_i,board_copy,-1,0)
            if ((row_i == 0 or seat_i == len(board_copy[row_i])-1)       or board_copy[row_i - 1][seat_i + 1] != '#'):
                available += 1
            if  (seat_i == len(board_copy[row_i])-1                     or board_copy[row_i][seat_i + 1] != '#'):
                available += 1
            if  ((row_i == len(board_copy)-1 or seat_i == len(board_copy[row_i])-1)  or board_copy[row_i+1][seat_i + 1] != '#'):
                available += 1
            if  (row_i == len(board_copy)-1                             or board_copy[row_i + 1][seat_i] != '#'):
                available += 1
            if  ((row_i == len(board_copy)-1 or seat_i == 0)            or board_copy[row_i + 1][seat_i - 1] != '#'):
                available += 1
            if  (seat_i == 0                                            or board_copy[row_i][seat_i - 1] != '#'):
                available += 1
            if  ((row_i == 0 or seat_i == 0)                             or board_copy[row_i-1][seat_i - 1] != '#'):
                available += 1
            if available == 8 and seat == "L":
                board[row_i][seat_i] = "#"
            if available < 5 and seat == "#": 
                board[row_i][seat_i] = "L"     
                pass
    board_count = 0
    board_copy_count = 0
    for row in board:
        board_count += row.count('#')
    for row in board_copy:
        board_copy_count += row.count('#')
    print(board_count)
    if board_copy_count == board_count:
        different = False
print("FINIISHED")




                