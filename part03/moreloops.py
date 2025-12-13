#1 Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:
#Sample output

#Please type in a number: 2
#1 x 1 = 1
#1 x 2 = 2
#2 x 1 = 2
#2 x 2 = 4
#Sample output

#Please type in a number: 3
#1 x 1 = 1
#1 x 2 = 2
#1 x 3 = 3
#2 x 1 = 2
#2 x 2 = 4
#2 x 3 = 6
#3 x 1 = 3
#3 x 2 = 6
#3 x 3 = 9
# Write your solution here
print(f'Exercício 1')
number = int(input('Please type in a number: '))
x = 1

while (x <= number):
    y = 1
    while y <= number:
        print(f'{x} x {y} = {x * y}')
        y += 1

    x += 1
#2 Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

#An example of expected behaviour:
#Sample output

#Please type in a sentence: Humpty Dumpty sat on a wall
#H
#D
#s
#o
#a
#w
# Write your solution here
print(f'Exercício 2')
sentence = input('Please type in a sentence: ')
findSpace = 0

while findSpace != -1 and len(sentence) != 0:
    if sentence[0] != ' ':
        print(sentence[0])

    findSpace = sentence.find(' ')

    if findSpace == -1:
        break

    sentence = sentence[findSpace + 1:]
    
#3 Please write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.

#The factorial of a number involves multiplying the number by all the positive integers smaller than itself. In other words, it is the product of all positive integers less than or equal to the number. For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

#Some examples of expected behaviour:
#Sample output

#Please type in a number: 3
#The factorial of the number 3 is 6
#Please type in a number: 4
#The factorial of the number 4 is 24
#Please type in a number: -1
#Thanks and bye!
#Sample output

#Please type in a number: 1
#The factorial of the number 1 is 1
#Please type in a number: 0
#Thanks and bye!
# Write your solution here
print(f'Exercício 3')
while True:
    number = int(input('Please type in a number: '))

    if number <= 0:
        print(f'Thanks and bye!')
        break
    
    res = 1
    x = number

    while x > 1:
        res *= x
        x -= 1

    print(f'The factorial of the number {number} is {res}')

#4 Please write a program which asks the user to type in a number. The program then prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.
#Sample output

#Please type in a number: 5
#2
#1
#4
#3
#5
#Sample output

#Please type in a number: 6
#2
#1
#4
#3
#6
#5
# Write your solution here
print(f'Exercício 4')
number = int(input('Please type in a number: '))
x = 2
y = 1

if number == 1:
    print(y)
else:
    while x <= number:
        print(x)
        print(y)

        x += 2
        y += 2

        if x > number and number % 2 != 0:
            print(y)
            break
        
#5 Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.
#Sample output

#Please type in a number: 5
#1
#5
#2
#4
#3
#Sample output

#Please type in a number: 6
#1
#6
#2
#5
#3
#4
# Write your solution here
print(f'Exercício 5')
number = int(input('Please type in a number: '))
x = 1
y = 0
z = number

while y < z and x != number:
    print(x)
    print(number)

    x += 1
    number -= 1
    y += 2

if x == number:
    print(x)

