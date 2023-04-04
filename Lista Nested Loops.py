#number_grid = [
#    1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
#]
#print(number_grid)

number_grid = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [123],
    [0, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [-1, -2, -3],
    [12 * 3],
    [12 - 6],
    [12 + 12],
]

#print(number_grid)

number_grid2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#print(number_grid2[2][1])

#for sequencia in number_grid2:
#    print(sequencia)

for sequencia in number_grid2:
    for coluna in sequencia:
        print(coluna)