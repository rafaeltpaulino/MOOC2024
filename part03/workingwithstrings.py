#1 Please write a program which asks the user for a string and an amount. The program then prints out the string as many times as specified by the amount. The printout should all be on one line, with no extra spaces or symbols added.

#An example of expected behaviour:
#Sample output

#Please type in a string: hiya
#Please type in an amount: 4
#hiyahiyahiyahiya
# Write your solution here
print(f'Exercício 1')
string = input('Please type in a string: ')
amount = int(input('Please type in a amount'))

print(string * amount)

#2 Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

#Some examples of expected behaviour:
#Sample output

#Please type in string 1: hey
#Please type in string 2: hiya
#hiya is longer
#Sample output

#Please type in string 1: howdy doody
#Please type in string 2: hola
#howdy doody is longer
#Sample output

#Please type in string 1: hey
#Please type in string 2: bye
#The strings are equally long
# Write your solution here
print(f'Exercício 2')
string1 = input('Please type in string 1: ')
string2 = input('Please type in string 2: ')

if len(string1) > len(string2):
    print(f'{string1} is longer')
elif len(string2) > len(string1):
    print(f'{string2} is longer')
else:
    print('The strings are equally long')

#3 Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

#An example of expected behaviour:
#Sample output

#Please type in a string: hiya
#a
#y
#i
#h
# Write your solution here
print(f'Exercício 3')
inputString = input('Please type in a string: ')
aux = -1

while aux >= -(len(inputString)):
    print(inputString[aux])
    aux -= 1

#4 Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.
#Sample output

#Please type in a string: python
#The second and the second to last characters are different
#Sample output

#Please type in a string: pascal
#The second and the second to last characters are a
# Write your solution here
print(f'Exercício 4')
inputString = input('Please type in a string: ')

if inputString[1] == inputString[-2]:
    print(f'The second and the second to last characters are {inputString[1]}')
else:
    print(f'The second and the second to last characters are different')
    
#5 Please write a program which prints out a line of hash characters, the width of which is chosen by the user.
#Sample output

#Width: 3

###

#Sample output

#Width: 8

########
# Write your solution here
print(f'Exercício 5')
width = int(input('Width: '))
hashes = ('#' * width)

print(hashes)

#6 Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.
#Sample output

#Width: 10
#Height: 3
##########
##########
##########

# Write your solution here
print(f'Exercício 6')
width = int(input('Width: '))
height = int(input('Height: '))

hashes = ('#' * width)

while height > 0:
    print(hashes)
    height -= 1

#7 Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.
#Sample output

#Please type in a string: Hi there!

#Hi there!
#---------

#Please type in a string: This is a test

#This is a test
#--------------

#Please type in a string: a

#a
#-

#Please type in a string:
# Write your solution here
print(f'Exercício 7')
inputString = input('Please type in a string: ')
underLine = '-'

while inputString:
    print(inputString)
    print(underLine * len(inputString))

    inputString = input('Please type in a string: ')

#8 Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

#You may assume the input string is at most 20 characters long.
#Sample output

#Please type in a string: python

#**************python

#Sample output

#Please type in a string: alongerstring

#*******alongerstring

#Sample output

#Please type in a string: averyverylongstring

#*averyverylongstring
# Write your solution here
print(f'Exercício 8')
inputString = input('Please type in a string: ')
compensation = ('*' * (20 - len(inputString)))

print(compensation + inputString)

#9 Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

#If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.
#Sample output

#Word: testing

#******************************
#*          testing           *
#******************************

#Sample output

#Word: python

#******************************
#*           python           *
#******************************
# Write your solution here
print(f'Exercício 9')
inputString = input('Word: ')
asterisks = ('*' * 30)
whiteSpace = (' ' * ((28 - len(inputString)) // 2))

if len(inputString) % 2 == 0:
    print(asterisks)
    print('*' + whiteSpace + inputString + whiteSpace + '*')
    print(asterisks)
else:
    print(asterisks)
    print('*' + (whiteSpace + ' ') + inputString + whiteSpace + '*')
    print(asterisks)

#10 Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. Have a look at the example below.
#Sample output

#Please type in a string: test
#t
#te
#tes
#test
# Write your solution here
print(f'Exercício 10')
inputString = input('Please type in a string: ')
x = 0

while x <= len(inputString):
    print(inputString[:x])
    x += 1

#11 Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.
#Sample output

#Please type in a string: test
#t
#st
#est
#test
# Write your solution here
inputString = input('Please type in a string: ')
x = -1

while x >= -(len(inputString)):
    print(inputString[x:])
    x -= 1

#12 Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o.

#You may assume the input will be in lowercase entirely. Have a look at the examples below.
#Sample output

#Please type in a string: hello there
#a not found
#e found
#o found
#Sample output

#Please type in a string: hiya
#a found
#e not found
#o not found
# Write your solution here
print(f'Exercício 12')
inputString = input('Please type in a string: ')

if ('a' in inputString):
    print(f'a found') 
else:
    print(f'a not found')

if ('e' in inputString):
    print(f'e found') 
else:
    print(f'e not found')

if ('o' in inputString):
    print(f'o found') 
else:
    print(f'o not found')
    
#13 Please write a program which asks the user to type in a string and a single character. The program then prints the first three character slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

#Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. In that case nothing should be printed out, and there should not be any indexing errors when executing the program.
#Sample output

#Please type in a word: mammoth
#Please type in a character: m
#mam
#Sample output

#Please type in a word: banana
#Please type in a character: n
#nan
#Sample output

#Please type in a word: tomato
#Please type in a character: x
#Sample output

#Please type in a word: python
#Please type in a character: n
# Write your solution here
print(f'Exercício 13')
inputString = input('Please type in a word: ')
character = input('Please type in a character: ')
substringStart = inputString.find(character)
substringEnd = substringStart + 3

if substringEnd <= len(inputString):
    print(inputString[substringStart:substringEnd])
    
#14 Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.
#Sample output

#Please type in a word: mammoth
#Please type in a character: m
#mam
#mmo
#mot
#Sample output

#Please type in a word: banana
#Please type in a character: n
#nan

#Hint the following example may give you some inspiration as to how this exercise could be tackled:

#word = input("Word: ")
#while True:
#    if len(word) == 0:
#        break
#    print(word)
#    word = word[2:]

#Sample output

#Word: mammoth
#mammoth
#mmoth
#oth
#h
# Write your solution here
print(f'Exercício 14')
inputString = input('Please type in a word: ')
character = input('Please type in a character: ')

while len(inputString) > 2:
    substringStart = inputString.find(character)

    if substringStart == -1:
        break

    substringEnd = substringStart + 3

    if(substringEnd <= len(inputString)):
        print(inputString[substringStart:substringEnd])

    inputString = inputString[(substringStart + 1):]


#15 Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

#In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

#Some examples of expected behaviour:
#Sample output

#Please type in a string: abcabc
#Please type in a substring: ab
#The second occurrence of the substring is at index 3.
#Sample output

#Please type in a string: methodology
#Please type in a substring: o
#The second occurrence of the substring is at index 6.
#Sample output

#Please type in a string: aybabtu
#Please type in a substring: ba
#The substring does not occur twice in the string.
# Write your solution here
print(f'Exercício 15')
inputString = input('Please type in a string: ')
originalStringLenght = len(inputString)
inputSubstring = input('Please type in a substring: ')
firstOccurance = inputString.find(inputSubstring)
secondOccurance = inputString[firstOccurance + len(inputSubstring):].find(inputSubstring)
diff = originalStringLenght - len(inputString[firstOccurance + len(inputSubstring):])

if secondOccurance == -1:
    print(f'The substring does not occur twice in the string.')
else:
    print(f'The second occurrence of the substring is at index {secondOccurance + diff}.')
