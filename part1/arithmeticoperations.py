#1 Please write a program which asks the user for a number. The program then prints out the number multiplied by five.

#The program should function as follows:
#Sample output

#Please type in a number: 3
#3 times 5 is 15
# Write your solution here
inputNumber = int(input('Please type in a number: '))
timesNumber = 5

print(f'{inputNumber} times {timesNumber} is {inputNumber * timesNumber}')

#2 Please write a program which asks the user for their name and year of birth. The program then prints out a message as follows:
#Sample output

#What is your name? Frances Fictitious
#Which year were you born? 1990
#Hi Frances Fictitious, you will be 31 years old at the end of the year 2021
# Write your solution here
name = input('What is your name? ')
birthYear = int(input('Which year were you born? '))
currentYear = 2021

print(f'Hi {name}, you will be {currentYear - birthYear} years old at the end of the year {currentYear}')

#3 Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.

#The program should function as follows:
#Sample output

#How many days? 1
#Seconds in that many days: 86400

#Another example:
#Sample output

#How many days? 7
#Seconds in that many days: 604800
# Write your solution here
numberDays = int(input('How many days? '))
secondsInDay = 24*3600

print(f'Seconds in that many days: {numberDays * secondsInDay}')

#4 This program asks the user for three numbers. The program then prints out their product, that is, the numbers multiplied by each other. There is, however, something wrong with the program - it doesn't work quite right, as you can see if you run it. Please fix it.

#An example of the expected execution of the program:
#Sample output

#Please type in the first number: 2
#Please type in the second number: 3
#Please type in the third number: 5
#The product is 30
# Fix the code
number = 1
number *= int(input("Please type in the first number: "))
number *= int(input("Please type in the second number: "))
number *= int(input("Please type in the third number: "))

print(f'The product is {number}')

#5 Please write a program which asks the user for two numbers. The program will then print out the sum and the product of the two numbers.

#The program should function as follows:
#Sample output

#Number 1: 3
#Number 2: 7
#The sum of the numbers: 10
#The product of the numbers: 21
# Write your solution here
number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))

print(f'The sum of the numbers: {number1 + number2}')
print(f'The product of the numbers: {number1 * number2}')

#6 Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

#The program should function as follows:
#Sample output

#Number 1: 2
#Number 2: 1
#Number 3: 6
#Number 4: 7
#The sum of the numbers is 16 and the mean is 4.0
# Write your solution here
number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
number3 = int(input('Number 3: '))
number4 = int(input('Number 4: '))
sum = number1 + number2 + number3 + number4

print(f'The sum of the numbers is {sum} and the mean is {sum / 4}')

#7 Please write a program which estimates a user's typical food expenditure.

#The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

#Based on this information the program calculates the user's typical food expenditure both weekly and daily.

#The program should function as follows:
#Sample output

#How many times a week do you eat at the student cafeteria? 4
#The price of a typical student lunch? 2.5
#How much money do you spend on groceries in a week? 28.5

#Average food expenditure:
#Daily: 5.5 euros
#Weekly: 38.5 euros
# Write your solution here
timesEatCafeteriaWeek = int(input('How many times a week do you eat at the student cafeteria? '))
priceStudentLunch = float(input('The price of a typical student lunch? '))
oneySpentGroceriesWeek = float(input('How much money do you spend on groceries in a week? '))

print(f'Average food expenditure:')

print(f'Daily: { ((priceStudentLunch * timesEatCafeteriaWeek) / 7) + (oneySpentGroceriesWeek / 7)} euros')

print(f'Weekly: {(priceStudentLunch * timesEatCafeteriaWeek) + oneySpentGroceriesWeek} euros')

#8 Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

#If you can't get your code working as expected, it is absolutely okay to move on and come back to this exercise later. The topic of the next section is conditional statements. This exercise can also be solved using a conditional construction.
#Sample output

#How many students on the course? 8
#Desired group size? 4
#Number of groups formed: 2
#Sample output

#How many students on the course? 11
#Desired group size? 3
#Number of groups formed: 4

#Hint: the integer division operator // could come in handy here.
# Write your solution here
numberSudentsCourse = int(input('How many students on the course? '))
sizeGroupStudents = int(input('Desired group size? '))
res = numberSudentsCourse // sizeGroupStudents

if(numberSudentsCourse % sizeGroupStudents == 0):
    print(f'Number of groups formed: {res}')
else:
    print(f'Number of groups formed: {res + 1}')