#1 lease write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.

#The beginning of your output should look like this:
#Sample output

#2
#4
#6
#8
#etc...
# Write your solution here
print(f'Exercício 1')
number = 2

while number <= 30:
    print(f'{number}')
    number += 2
    
#2 The program below has some syntactic issues:

#print("Are you ready?")
#number = int(input("Please type in a number: "))
#while number = 0:
#print(number)
#print("Now!")

#Please fix it so that it prints out the following:
#Sample output

#Are you ready?
#Please type in a number: 5
#5
#4
#3
#2
#1
#Now!
# Fix the program
print(f'Exercício 2')
print("Are you ready?")

number = int(input("Please type in a number: "))

while number > 0:
    print(number)
    number -= 1

print("Now!")

#3 Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.
#Sample output

#Upper limit: 5
#1
#2
#3
#4

#Please don't use the value True as the condition of your while loop in this exercise!
# Write your solution here
print(f'Exercício 3')
number = int(input('Upper limit: '))
x = 1

while x < number:
    print(x)
    x += 1
    
#4 Please write a program which asks the user to type in an upper limit. The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. That is, the program prints out powers of two in order.

#The execution of the program finishes when the next number to be printed would be greater than the limit set by the user. No numbers greater than the limit should be printed.
#Sample output

#Upper limit: 8
#1
#2
#4
#8
#Sample output

#Upper limit: 20
#1
#2
#4
#8
#16
#Sample output

#Upper limit: 100
#1
#2
#4
#8
#16
#32
#64

#Please don't use the value True as the condition of your while loop in this exercise!

#What are powers of two? The first power of two is the number 1. The next one is 1 times 2, which is 2. The next is 2 times 2, which is 4. The next is 4 times 2, which is 8, and so forth. Each power in the sequence is multiplied by two to produce the next one.
# Write your solution here
print(f'Exercício 4')
limit = (int(input('Upper limit: ')))
x = 1

while x <= limit:
    print(x)
    x *= 2
    
#5 Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).
#Sample output

#Upper limit: 27
#Base: 3
#1
#3
#9
#27
#Sample output

#Upper limit: 1234567
#Base: 10
#1
#10
#100
#1000
#10000
#100000
#1000000

#Please don't use the value True as the condition of your while loop in this exercise!
# Write your solution here
print(f'Exercício 5')
limit = int(input('Upper limit: '))
base = int(input('Base: '))
x = 1

while x <= limit:
    print(x)
    x *= base
    
#6 Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. The program should function as follows:
#Sample output

#Limit: 2
#3
#Sample output

#Limit: 10
#10
#Sample output

#Limit: 18
#21

#If you have trouble understanding how the desired output is calculated, the sample outputs in the next exercise may help. You may assume the number typed in by the user is always equal to 2 or higher.
# Write your solution here
print(f'Exercício 6')
limit = int(input('Limit: '))
x = 1
aux = 1

while x < limit:
    aux += 1
    x += aux

print(x)

#7 Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:
#Sample output

#Limit: 2
#The consecutive sum: 1 + 2 = 3
#Sample output

#Limit: 10
#The consecutive sum: 1 + 2 + 3 + 4 = 10
#Sample output

#Limit: 18
#The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

#You may assume the number typed in by the user is always equal to 2 or higher.
# Write your solution here
print(f'Exercício 7')
limit = int(input('Limit: '))
x = 1
aux = 1
printSum = 'The consecutive sum: 1'

while x < limit:
    aux += 1
    x += aux
    printSum += f' + {aux}'

printSum += f' = {x}'
print(printSum)