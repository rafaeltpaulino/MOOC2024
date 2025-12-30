'''
Please write a function named double_items(numbers: list), which takes a list of integers as its argument.

The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.

An example of the function at work:

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)

Sample output

original: [2, 4, 5, 3, 11, -4]
doubled: [4, 8, 10, 6, 22, -8]
'''
# Write your solution here
def double_items(numbers: list[int]) -> list[int]:
    return [number * 2 for number in numbers]

if __name__ == '__main__':
    print('Exercício 1')
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
    
'''
Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.

The functions should find and remove the smallest item in the list. You may assume there is a single smallest item in the list.

The function should not have a return value - it should directly modify the list it receives as a parameter.

An example of how the function works:

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)

Sample output

[2, 4, 6, 3, 5]
'''
# Write your solution here
def remove_smallest(numbers: list[int]):
    numbers.remove(min(numbers))
    
    
if __name__ == '__main__':
    print('Exercício 2')
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
    
'''
In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.

The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should print out the grid in the format specified in the examples below.

The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.

sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)

Sample output

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Three numbers added:

2 _ _  _ _ _  _ _ _
_ _ 7  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ 3 _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Hint

Remember it is possible to call the print function without causing a line change:

print("characters ", end="")
print("without carriage returns", end="")

Sample output

characters without carriage returns

Sometimes you need just a new line, which a print statement without any argument will achieve:

print()
'''
# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(9):
        if i == 3 or i == 6:
            print()
            
        for j in range(9):
            if sudoku[i][j] == 0:
                print('_', end="")
            else:
                print(sudoku[i][j], end="")
            
            if (j == 2 or j == 5) and j != 8:
                print('  ', end="")
            else:
                print(' ', end="")
                
        print()
            

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

if __name__ == '__main__':
    print('Exercício 3')
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)

'''
This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.

The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.

The print_sudoku function from the previous exercise could be useful for testing, and it is used in the example below:

sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

grid_copy = copy_and_add(sudoku, 0, 0, 2)
print("Original:")
print_sudoku(sudoku)
print()
print("Copy:")
print_sudoku(grid_copy)

Sample output

Original:
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Copy:
2 _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Hint When dealing with nested lists you should be extra careful when copying. What all needs to be explicitly copied, and where do changes actually have an effect? The visualisation tool is a great help here, too, although the size of the sudoku grid will make the view less orderly than usual.
'''
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    newSudoku = []
    i = 0
    
    for row in sudoku:
        newSudoku.append([])
        for item in row:
            newSudoku[i].append(item)
        
        i += 1
    
    newSudoku[row_no][column_no] = number
    
    return newSudoku
    
if __name__ == '__main__':
    print('Exercício 4')
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)

'''
Tic-Tac-Toe is played on a 3 by 3 grid, by two players who take turns inputting noughts and crosses. If either player succeeds in placing three of their own symbols on any row, column or diagonal, they win. If neither player manages this, it is a draw.

Please write a function named play_turn(game_board: list, x: int, y: int, piece: str), which places the given symbol at the given coordinates on the board. The values of the coordinates on the board are between 0 and 2.

NB: when compared to the sudoku exercises, the arguments the function takes are the other way around here. The column x comes first, and the row y second.

The board consists of the following strings:

    "": empty square
    "X": player 1 symbol
    "O": player 2 symbol

The function should return True if the square was empty and the symbol was successfully placed on the game board. The function should return False if the square was occupied, or if the coordinates weren't valid.

An example execution of the function:

game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
print(play_turn(game_board, 2, 0, "X"))
print(game_board)

Sample output

True
[['', '', 'X'], ['', '', ''], ['', '', '']]
'''
# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    if x < 0 or x > 2 or y < 0 or y > 2 or game_board[y][x] != '':
        return False
    else:
        game_board[y][x] = piece
        return True
    
if __name__ == '__main__':
    print('Exercício 5')
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)
    
'''
Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.

The following matrix

1 2 3
4 5 6
7 8 9

transposed looks like this:

1 4 7
2 5 8
3 6 9

The function should not have a return value. The matrix should be modified directly through the reference.
'''
# Write your solution here
def print_matrix(matrix : list):
    for row in matrix:
        print(row)

def transpose(matrix: list):
    matrixLen = len(matrix)
    
    for i in range(matrixLen - 1):
        for j in range(i + 1, matrixLen):
            temp  = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = temp
            
if __name__ == '__main__':
    print('Exercício 6')
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    transpose(matrix)
    print_matrix(matrix)