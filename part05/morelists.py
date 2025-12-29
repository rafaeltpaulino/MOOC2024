'''
Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.

An example of expected behaviour:


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

Sample output

howdydoody
'''
# Write your solution here
def longest(strings: list[str]) -> str:
    res = strings[0]
    
    for string in strings:
        if len(string) > len(res):
            res = string
            
    return res


if __name__ == "__main__":
    print('Exercício 1')
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

'''
Please write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer value as its arguments. The function then counts how many elements within the matrix match the argument value.

An example of how the function should work:

m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1))

Sample output

3
'''
# Write your solution here
def count_matching_elements(my_matrix: list[int], element: int) -> int:
    res = 0
    
    for row in my_matrix:
        for number in row:
            if number == element:
                res += 1
                
    return res


if __name__ == '__main__':
    print('Exercício 2')
    m = [[1, 0, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 0))
    
'''
In a game of Go two players take turns to place black and white stones on a game board. The winner is the player who manages to encircle a bigger area on the board with their own game pieces.

Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. The array consists of integer values, which represent the following situations:

    0: empty square
    1: player 1 game piece
    2: player 2 game piece

The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. Also, the size of the game board is not limited.

The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If both players have the same number of pieces on the board, the function should return the value 0.
'''
# Write your solution here
def who_won(game_board: list[int]) -> int:
    print('Exercício 3')
    p1Points = 0
    p2Points = 0
    
    for row in game_board:
        for number in row:
            if number == 1:
                p1Points += 1
                
            if number == 2:
                p2Points += 1
                
    if p1Points > p2Points:
        return 1
    elif p2Points > p1Points:
        return 2
    else:
        return 0
    
'''
Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.

The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(row_correct(sudoku, 0))
print(row_correct(sudoku, 1))

Sample output

True
False
'''
# Write your solution here
def row_correct(sudoku: list[int], row_no: int) -> bool:
    for i in range(1, 9):
        if sudoku[row_no][i] < 0 or sudoku[row_no][i] > 9:
            return False
        
        if sudoku[row_no][i] != 0:            
            for j in range(0, i):
                if sudoku[row_no][i] == sudoku[row_no][j]:
                    return False
                
    return True
        
if __name__ == "__main__":
    print('Exercício 4')
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))
    
'''
Please write a function named column_correct(sudoku: list, column_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single column, as its arguments. Columns are indexed from 0.

The function should return True or False, depending on whether the column is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(column_correct(sudoku, 0))
print(column_correct(sudoku, 1))

Sample output

False
True
'''
# Write your solution here
def column_correct(sudoku: list[int], column_no: int) -> bool:
    numbers = []
    
    for i in range(9):
        if sudoku[i][column_no] < 0 or sudoku[i][column_no] > 9:
            return False
        
        if sudoku[i][column_no] > 0:
            if sudoku[i][column_no] in numbers:
                return False
            
            numbers.append(sudoku[i][column_no])
            
    return True

if __name__ == "__main__":
    print('Exercício 5')
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    
    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))
    
'''
Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments. Rows and columns are indexed from 0.

The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. That is, whether the block contains each of the numbers 1 to 9 at most once.

Notice that this function does not strictly follow the rules of sudoku. In a real game of sudoku there are only 9 blocks to check, and these are located at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6). Such restrictions on indexes should not be implemented here.

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(block_correct(sudoku, 0, 0))
print(block_correct(sudoku, 1, 2))

Sample output

False
True

The first function call should check the 3 by 3 block beginning with the square at indexes 0, 0:

9 0 0
2 0 0
0 2 0

The second function call should check the 3 by 3 block beginning with the square at row 1, column 2:

0 2 5
0 3 0
4 0 0

This second block would not be checked in an actual game of sudoku, but your function should allow for it to be checked.
'''
# Write your solution here
def block_correct(sudoku: list[int], row_no: int, column_no: int) -> bool:
    numbers = []
    
    for i in range(row_no, row_no + 3):
        temp = sudoku[i]
        
        for j in range(column_no, column_no + 3):
                if temp[j] > 0 and temp[j] in numbers:
                    return False
                
                numbers.append(temp[j])
            
    return True


if __name__ == "__main__":
    print('Exercício 6')
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))
    
'''
Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument. The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. Copy the functions from the exercises above into your Python code file for this exercise.

The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the numbers 1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns False.

The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders. These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))

Sample output

False
True
'''
# Write your solution here
def row_correct(sudoku: list[int], row_no: int) -> bool:
    numbers = []
        
    for item in sudoku[row_no]:
            if item > 0 and item in numbers:
                return False
            
            numbers.append(item)
                    
    return True

def column_correct(sudoku: list[int], column_no: int) -> bool:
    numbers = []
    
    for i in range(9):
        if sudoku[i][column_no] < 0 or sudoku[i][column_no] > 9:
            return False
        
        if sudoku[i][column_no] > 0:
            if sudoku[i][column_no] in numbers:
                return False
            
            numbers.append(sudoku[i][column_no])
            
    return True

def block_correct(sudoku: list[int], row_no: int, column_no: int) -> bool:
    numbers = []
    
    for i in range(row_no, row_no + 3):
        temp = sudoku[i]
    
        for j in range(column_no, column_no + 3):
                if temp[j] > 0 and temp[j] in numbers:
                    return False
                
                numbers.append(temp[j])
            
    return True

def sudoku_grid_correct(sudoku: list[int]) -> bool:
    blockRow = 0
    blockCol = 0
    
    for i in range(9):
        row = row_correct(sudoku, i)
        column = column_correct(sudoku, i)
        block = block_correct(sudoku, blockRow, blockCol)
        
        blockCol += 3
        
        if blockCol > 6:
            blockRow += 3 
            blockCol = 0
        
        if (not row) or (not column) or (not block):
            return False
        
    return True    
        
        
if __name__ == '__main__':
    print('Exercício 7')
    sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]  ]

    print(sudoku_grid_correct(sudoku2))