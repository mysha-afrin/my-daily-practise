#exercise
#create the fields for a chess board
#abcdefgh
#12345678

chess_board = [[(x, y) for x in range(1, 8)] for y in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
for row in chess_board:
    print(row)
