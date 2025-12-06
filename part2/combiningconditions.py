#1 Please write a program which asks for the user's age. If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.

#Have a look at the examples of expected behaviour below to figure out which comment is applicable in each case.
#Sample output

#What is your age? 13
#Ok, you're 13 years old
#Sample output

#What is your age? 2
#I suspect you can't write quite yet...
#Sample output

#What is your age? -4
#That must be a mistake
# Write your solution here
print(f'Exercício 1')
userAge = int(input('What is your age? '))

if userAge < 0:
    print(f'That must be a mistake')
elif userAge < 5:
    print(f"I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {userAge} years old")
    
#2 Please write a program which asks for the user's name. If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

#In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

#Some examples:
#Sample output

#Please type in your name: Morty
#I think you might be one of Mickey Mouse's nephews.
#Sample output

#Please type in your name: Huey
#I think you might be one of Donald Duck's nephews.
#Sample output

#Please type in your name: Ken
#You're not a nephew of any character I know of.
# Write your solution here
print(f'Exercício 2')
userName = input('Please type in your name: ')

if (userName == 'Huey') or (userName == 'Dewey') or (userName == 'Louie'):
    print(f"I think you might be one of Donald Duck's nephews.")
elif (userName == 'Morty') or (userName == 'Ferdie'):
    print(f"I think you might be one of Mickey Mouse's nephews.")
else:
    print(f"You're not a nephew of any character I know of.")
    
#3 The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.
#points	grade
#< 0	impossible!
#0-49	fail
#50-59	1
#60-69	2
#70-79	3
#80-89	4
#90-100	5
#> 100	impossible!

#Some examples:
#Sample output

#How many points [0-100]: 37
#Grade: fail
#Sample output

#How many points [0-100]: 76
#Grade: 3
#Sample output

#How many points [0-100]: -3
#Grade: impossible!
# Write your solution here
print(f'Exercício 3')
points = int(input('How many points [0-100]: '))

if (points < 0) or (points > 100):
    print(f'Grade: impossible!')
elif points < 50:
    print(f'Grade: fail')
elif points < 60:
    print(f'Grade: 1')
elif points < 70:
    print(f'Grade: 2')
elif points < 80:
    print(f'Grade: 3')
elif points < 90:
    print(f'Grade: 4')
elif points <= 100:
    print(f'Grade: 5')

#4 Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.

#Some examples of expected behaviour:
#Sample output

#Number: 9
#Fizz
#Sample output

#Number: 7
#Sample output

#Number: 20
#Buzz
#Sample output

#Number: 45
#FizzBuzz
# Write your solution here
print(f'Exercício 4')
number = int(input('Number: '))

if (number % 3 == 0) and (number % 5 == 0):
    print(f'FizzBuzz')
elif (number % 3 == 0):
    print(f'Fizz')
elif (number % 5 == 0):
    print(f'Buzz')
    
#5 Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

#Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

#Some examples:
#Sample output

#Please type in a year: 2011
#That year is not a leap year.
#Sample output

#Please type in a year: 2020
#That year is a leap year.
#Sample output

#Please type in a year: 1800
#That year is not a leap year.
# Write your solution here
print(f'Exercício 5')
year = int(input('Please type in a year: '))

if (year % 100 == 0) and (year % 400 == 0):
    print(f'That year is a leap year.')
elif not(year % 100 == 0) and (year % 4 == 0):
    print(f'That year is a leap year.')
else:
    print(f'That year is not a leap year.')
    
#6
#Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

#You may assume the letters will be either all uppercase, or all lowercase.

#Some examples of expected behaviour:
#Sample output

#1st letter: x
#2nd letter: c
#3rd letter: p
#The letter in the middle is p
#Sample output

#1st letter: C
#2nd letter: B
#3rd letter: A
#The letter in the middle is B
# Write your solution here
print(f'Exercício 6')
letter1 = input('1st letter: ')
letter2 = input('2nd letter: ')
letter3 = input('3rd letter: ')

if (letter1 > letter2 and letter1 < letter3) or (letter1 < letter2 and letter1 > letter3):
    print(f'The letter in the middle is {letter1}')

if (letter2 > letter1 and letter2 < letter3) or (letter2 < letter1 and letter2 > letter3):
    print(f'The letter in the middle is {letter2}')

if (letter3 > letter1 and letter3 < letter2) or (letter3 < letter1 and letter3 > letter2):
    print(f'The letter in the middle is {letter3}')
    
#7 Some say paying taxes makes Finns happy, so let's see if the secret of happiness lies in one of the taxes set out in Finnish tax code.

#According to the Finnish Tax Administration, a gift is a transfer of property to another person against no compensation or payment. If the total value of the gifts you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.

#When the gift is received from a close relative or a family member, the amount of tax to be paid is determined by the following table, which is also available on this website:
#Value of gift	Tax at the lower limit	Tax rate for the exceeding part (%)
#5 000 — 25 000	100	8
#25 000 — 55 000	1 700	10
#55 000 — 200 000	4 700	12
#200 000 — 1 000 000	22 100	15
#1 000 000 —	142 100	17

#So, for a gift of 6 000 euros the recipient pays a tax of 180 euros (100 + (6 000 - 5 000) * 0.08). Similarly, for a gift of 75 000 euros the recipient pays a tax of 7 100 euros (4 700 + (75 000 - 55 000) * 0.12).

#Please write a program which calculates the correct amount of tax for a gift from a close relative. Have a look at the examples below to see what is expected. Notice the lack of thousands separators in the input values - you may assume there will be no spaces or other thousands separators in the numbers in the input, as we haven't yet covered dealing with these.
#Sample output

#Value of gift: 3500
#No tax!
#Sample output

#Value of gift: 5000
#Amount of tax: 100.0 euros
#Sample output

#Value of gift: 27500
#Amount of tax: 1950.0 euros
# Write your solution here
print(f'Exercício 7')
giftValue = int(input('Value of gift: '))

if giftValue < 5000:
    print(f'No tax!')
elif giftValue < 25000:
    print(f'Amount of tax: {100 + (giftValue - 5000) * 0.08}')
elif giftValue < 55000:
    print(f'Amount of tax: {1700 + (giftValue - 25000) * 0.10}')
elif giftValue < 200000:
    print(f'Amount of tax: {4700 + (giftValue - 55000) * 0.12}')
elif giftValue < 1000000:
    print(f'Amount of tax: {22100 + (giftValue - 200000) * 0.15}')
else:
    print(f'Amount of tax: {142100 + (giftValue - 1000000) * 0.17}')
