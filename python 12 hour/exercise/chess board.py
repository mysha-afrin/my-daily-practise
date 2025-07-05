#exercise
#create the fields for a chess board
#abcdefgh
#12345678


chess_board = [[f'{letter}{num}'for num in range(1,9)]for letter in 'ABCDEFGH']
for row in chess_board:
    print(row)
