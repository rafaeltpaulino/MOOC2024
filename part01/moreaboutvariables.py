#1 Your friend is working on an app for jobseekers. She sends you this bit of code:

#name = "Tim Tester"
#age = 20
#skill1 = "python"
#level1 = "beginner"
#skill2 = "java"
#level2 = "veteran"
#skill3 = "programming"
#level3 = "semiprofessional"
#lower = 2000
#upper = 3000

#print("my name is ", name, " , I am ", age, "years old")
#print("my skills are")
#print("- ", skill1, " (", level1, ")")
#print("- ", skill2, " (", level2, ")")
#print("- ", skill3, " (", level3, " )")
#print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")

#The program should print out exactly the following:

#my name is Tim Tester, I am 20 years old

#my skills are
# - python (beginner)
# - java (veteran)
# - programming (semiprofessional)

#I am looking for a job with a salary of 2000-3000 euros per month

#The code works almost correctly, but not quite. This exercise has very strict tests, which check the output for every single bit of whitespace.

#Please fix the code so that the printout looks right. Notice especially how the comma notation in the print command automatically inserts a space around the different comma-separated parts.

#The easiest way to transform the code so that it meets requirements is to use f-strings.

#Hint: you can print an empty line by adding an empty print command, or by adding the newline character \n into your string.

#Do remember to be extra careful when formatting printouts also in the future on this course. Some of the exercises have tests that require your output to be exactly as specified in the examples given. For example, please use actual whitespace characters in your code, instead of ASCII character codes for whitespace, or some such.

# Write your solution here
print('Exercicio 1')
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f'my name is {name}, I am {age} years old \n')
print(f'my skills are')
print(f' - {skill1} ({level1})')
print(f' - {skill2} ({level2})')
print(f' - {skill3} ({level3})')
print('')
print(f'I am looking for a job with a salary of {lower}-{upper} euros per month')

#2 This program already contains two integer variables, x and y:

#x = 27
#y = 15

#Please complete the program so that it also prints out the following:
#Sample output

#27 + 15 = 42
#27 - 15 = 12
#27 * 15 = 405
#27 / 15 = 1.8

#The program should work correctly even if the values of the variables are changed. That is, if the first two lines are replaced with this

#x = 4
#y = 9

#the program should print out the following:
#Sample output

#4 + 9 = 13
#4 - 9 = -5
#4 * 9 = 36
#4 / 9 = 0.4444444444444444

# Write your solution here
print('Exercicio 2')
x = 27
y = 15
sum = x + y 
subtraction = x - y 
multiplication = x * y 
division = x / y 

print(f'{x} + {y} = {sum}')
print(f'{x} - {y} = {subtraction}')
print(f'{x} * {y} = {multiplication}')
print(f'{x} / {y} = {division}')

#3 Each print command usually prints out a line of its own, complete with a change of line at the end. However, if the print command is given an additional argument end = "", it will not print a line change.

#For example:

#print("Hi ", end="")
#print("there!")

#Sample output

#Hi there!

#Please fix this program so that the entire calculation, complete with result, is printed out on a single line. Do not change the number of print commands used.


#print(5)
#print(" + ")
#print(8)
#print(" - ")
#print(4)
#print(" = ")
#print(5 + 8 - 4)

# Fix the code
print('Exercicio 3')
print(5, end='')
print(" + ", end='')
print(8, end='')
print(" - ", end='')
print(4, end='')
print(" = ", end='')
print(5 + 8 - 4, end='')