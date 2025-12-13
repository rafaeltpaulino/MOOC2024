'''
1 Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.

An example of expected behaviour:

line(7, "%")
line(10, "LOL")
line(3, "")

Sample output

%%%%%%%
LLLLLLLLLL
***
'''
# Write your solution here
def line(num, string):
    temp = ''
    
    if len(string) == 0:
        temp = ('*' * num)
    else:
        temp = (string[0] * num)
        
    print(temp)
    
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 1')
    line(5, "x")
    line(10, '')
    line(4, 'corinthians')
    
'''
2 Please write a function named box_of_hashes, which prints out a rectangle of hash characters. The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in your line function.

Some examples of how the function should work:

box_of_hashes(5)
print()
box_of_hashes(2)

Sample output

##########
##########
##########
##########
##########

##########
##########
'''
# Write your solution here
def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = 0
    while i < height:
        line(10, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 2')
    box_of_hashes(5)
    print()
    box_of_hashes(2)
    
'''
3 Please write a function named square_of_hashes, which draws a square of hash characters. The function takes one argument, which determines the length of the side of the square.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

square_of_hashes(5)
print()
square_of_hashes(3)

Sample output

#####
#####
#####
#####
#####

###
###
###
'''
# Write your solution here
def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = 0
    
    while i < size:
        line(size, "#")
        i += 1
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 3')
    square_of_hashes(5)
    print()
    square_of_hashes(3)
    
'''
4 Please write a function named square, which prints out a square of characters, and takes two arguments. The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

square(5, "*")
print()
square(3, "o")

Sample output

*****
*****
*****
*****
*****

ooo
ooo
ooo
'''
def square(size, character):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        line(size, character)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 4')
    square(5, "x")
    print()
    square(3, "y")
    
'''
5 Please write a function named triangle, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

triangle(6)
print()
triangle(3)

Sample output

#
##
###
####
#####
######

#
##
###
'''
def triangle(size):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(i, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 5')
    triangle(5)
    print()
    triangle(3)
    
'''
6 Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")

Sample output

X
XX
XXX
XXXX
XXXXX
*****
*****
*****

o
oo
++
++
++
++

.
..
...
'''
def shape(num1, string1, num2, string2):
    i = 1
    j = 0
    
    while i <= num1:
        line(i, string1)
        i += 1
    
    while j < num2:
        line(num1, string2)
        j += 1
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 6')
    shape(5, "x", 2, "o")
    print()
    shape(3, ".", 0, ",")
    print()
    shape(2, "o", 4, "+")
    
'''
7 Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

Calling spruce(3) should print out
Sample output

a spruce!
  *
 ***
*****
  *

Calling spruce(5) should print out
Sample output

a spruce!
    *
   ***
  *****
 *******
*********
    *

NB: to the left of the spruce there should be exactly the right amount of whitespace. If the shape of the spruce looks correct, but the left edge of the tree is not touching the left edge of the text area in the terminal, the tests will not accept the solution.
'''
# Write your solution here
def spruce(size):
    asterisk = '*'
    i = 0
    aux = 1
    j = size
    
    print('a spruce!')
    
    while i < size:
        print(' ' * (j - 1), end='')
        j -= 1
        
        print(asterisk * aux)
        aux += 2  
        i += 1  
    
    print(' ' * (size - 1), end='')     
    print('*')
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
    print()
    spruce(3)
    
'''
8 Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three.

An example of how the function is used:

print(greatest_number(3, 4, 1)) # 4
print(greatest_number(99, -4, 7)) # 99
print(greatest_number(0, 0, 0)) # 0
'''
# Write your solution here
def greatest_number(x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 8')
    greatest = greatest_number(5, 4, 8)
    print(greatest)
    greatest = greatest_number(7, 7, 7)
    print(greatest)
    greatest = greatest_number(10, 2, 9)
    print(greatest)
    greatest = greatest_number(-10, 5, 2)
    print(greatest)
    
'''
9 Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.

Some examples of how the function is used:

# same characters m and m
print(same_chars("programmer", 6, 7)) # True

# different characters p and r
print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
print(same_chars("programmer", 0, 12)) # False
'''
# Write your solution here
def same_chars(string, index1, index2):
    if index1 < 0 or index1 >= len(string):
        return False
    
    if index2 < 0 or index2 >= len(string):
        return False

    if string[index1] == string[index2]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("programmer", 6, 7))
    print(same_chars("prograMmer", 6, 7))
    print(same_chars("prograMmer", -1, 15))
    print(same_chars("prograMmer", 6, 7))
    print(same_chars("arara", 0, 2))
    
'''
10 Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.

In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. There will be no spaces in the beginning or at the end of the argument strings.

sentence = "it was a dark and stormy python"

print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python

Sample output

it
was
python

sentence = "it was"

print(second_word(sentence)) # was
print(last_word(sentence)) # was
'''
# Write your solution here
# Write your solution here
def find_word(sentence, posWord):
    word = sentence.split()
    
    return word[posWord]

def first_word(sentence):
    return find_word(sentence, 0)

def second_word(sentence):
    return find_word(sentence, 1)

def last_word(sentence):
    return find_word(sentence, -1)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    sentence = "it was a dark and stormy python"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    sentence = "it was"
    print(second_word(sentence))
    print(last_word(sentence))