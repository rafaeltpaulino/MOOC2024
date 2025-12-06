#1 Please write a program which asks the user for their age. The program should then print out a message based on whether the user is of age or not, using 18 as the age of maturity.

#Some examples of expected behaviour:
#Sample output

#How old are you? 12
#You are not of age!
#Sample output

#How old are you? 32
#You are of age!
# Write your solution here
print(f'Exercício 1')
ageOfMaturity = 18
userAge = int(input('How old are you? '))

if userAge < ageOfMaturity:
    print('You are not of age!')
else:
    print('You are of age!')

#2 Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.

#Some examples of expected behaviour:
#Sample output

#Please type in the first number: 5
#Please type in another number: 3
#The greater number was: 5
#Sample output

#Please type in the first number: 5
#Please type in another number: 8
#The greater number was: 8
#Sample output

#Please type in the first number: 5
#Please type in another number: 5
#The numbers are equal!
# Write your solution here
print(f'Exercício 2')
number1 = int(input('Please type in the first number: '))
number2 = int(input('Please type in the first number: '))

if number1 > number2:
    print(f'The greater number was: {number1}')
elif number2 > number1:
    print(f'The greater number was: {number2}')
else:
    print(f'The numbers are equal!')
    
#3 Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

#Some examples of expected behaviour:
#Sample output

#Person 1:
#Name: Alan
#Age: 26
#Person 2:
#Name: Ada
#Age: 27
#The elder is Ada
#Sample output

#Person 1:
#Name: Bill
#Age: 1
#Person 2:
#Name: Jean
#Age: 1
#Bill and Jean are the same age
# Write your solution here
print(f'Exercício 3')
print(f'Person 1:')
namePerson1 = input('Name: ')
agePerson1 = int(input('Age: '))
print(f'Person 2:')
namePerson2 = input('Name: ')
agePerson2 = int(input('Age: '))

if agePerson1 > agePerson2:
    print(f'The elder is {namePerson1}')
elif agePerson2 > agePerson1:
    print(f'The elder is {namePerson2}')
else:
    print(f'{namePerson1} and {namePerson2} are the same age')
    
#4 Python comparison operators can also be used on strings. String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if

    #the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
    #only the standard English alphabet of a to z, or A to Z, is used.

#Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

#You can assume all words will be typed in lowercase entirely.

#Some examples of expected behaviour:
#Sample output

#Please type in the 1st word: car
#Please type in the 2nd word: scooter
#scooter comes alphabetically last.
#Sample output

#Please type in the 1st word: zorro
#Please type in the 2nd word: batman
#zorro comes alphabetically last.
#Sample output

#Please type in the 1st word: python
#Please type in the 2nd word: python
#You gave the same word twice.
# Write your solution here
print(f'Exercício 4')
word1 = input('Please type in the 1st word: ')
word2 = input('Please type in the 2nd word: ')

if word1 > word2:
    print(f'{word1} comes alphabetically last.')
elif word2 > word1:
    print(f'{word2} comes alphabetically last.')
else:
    print(f'You gave the same word twice.')

