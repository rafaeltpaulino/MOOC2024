#1 Please write a function named seven_brothers. When the function is called, it should print out the names of the seven brothers in alphabetical order, as in the example below. See the similarly named exercise in part 1 for more details about the brothers.
#Sample output

#Aapo
#Eero
#Juhani
#Lauri
#Simeoni
#Timo
#Tuomas
# Write your solution here
# You can test your function by calling it within the following block
# if __name__ == "__main__":
#   seven_brothers()
def seven_brothers():
    print('Exercício 1')
    print('Aapo')
    print('Eero')
    print('Juhani')
    print('Lauri')
    print('Simeoni')
    print('Timo')
    print('Tuomas')

if __name__ == "__main__":
    seven_brothers()

#2 The exercise contains the outline of the function first_character. Please complete it so that it prints out the first character of the string it takes as its argument.

#def first_character(text):
     # write your code here

# testing the function:
#if __name__ == "__main__":
#    first_character('python')
#    first_character('yellow')
#    first_character('tomorrow')
#    first_character('heliotrope')
#    first_character('open')
#    first_character('night')

#Sample output

#p
#y
#t
#h
#o
#n
def first_character(text):
    print(text[0])
# write your code here
#
# testing the function:
if __name__ == "__main__":
    print('Exercício 2')
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

#3 Please write a function named mean, which takes three integer arguments. The function should print out the arithmetic mean of the three arguments.

#mean(5, 3, 1)
#mean(10, 1, 1)

#Sample output

#3.0
#4.0
# Write your code here
def mean(x, y, z):
    print(f'{(x + y + z) / 3}')
# Testing the function
if __name__ == "__main__":
    print('Exercício 3')
    mean(10, 1, 1)
    
#4 Please write a function named print_many_times(text, times), which takes a string and an integer as arguments. The integer argument specifies how many times the string argument should be printed out:

#print_many_times("hi", 5)

#print()

#text = "All Pythons, except one, grow up"
#times = 3
#print_many_times(text, times)

#Sample output

#hi
#hi
#hi
#hi
#hi

#All Pythons, except one, grow up.
#All Pythons, except one, grow up.
#All Pythons, except one, grow up.
# Write your solution here
def print_many_times(text, times):
    x = 0
    while x < times:
        print(text)
        x += 1 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 4')
    print_many_times("python", 5)
    
#5 Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square.

#hash_square(3)
#print()
#hash_square(5)

#Sample output

###
###
###

#####
#####
#####
#####
#####
# Write your solution here
def hash_square(length):
    hashes = ('#' * length)
    x = 0
    while x < length:
        print(hashes)
        x += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 5')
    hash_square(5)
    hash_square(2)
    
#6 Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:

#chessboard(3)
#print()
#chessboard(6)

#Sample output

#101
#010
#101

#101010
#010101
#101010
#010101
#101010
#010101
# Write your solution here
def chessboard(num):
    line1 = ''
    line2 = ''
    x = 0

    while x < num:
        if x % 2 == 0:
            line1 += '1'
        else:
            line1 += '0'

        x += 1

    x = 0

    while x < num:
        if x % 2 == 0:
            line2 += '0'
        else:
            line2 += '1'

        x += 1

    x = 0

    while x < num:
        if x % 2 == 0:
            print(line1)
        else:
            print(line2)

        x += 1
# Testing the function
if __name__ == "__main__":
    print('Exercício 6')
    chessboard(3)

#7 Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

#squared("ab", 3)
#print()
#squared("aybabtu", 5)

#Sample output

#aba
#bab
#aba

#aybab
#tuayb
#abtua
#ybabt
#uayba
# Write your solution here
def squared(string, num):
    temp = (string * 1000000)
    i = 0

    while i < num:
        print(temp[0:num])
        temp = temp[num:]
        i += 1

if __name__ == "__main__":
    print('Exercício 7')
    squared('aybabtu', 5)
    squared('ab', 3)

