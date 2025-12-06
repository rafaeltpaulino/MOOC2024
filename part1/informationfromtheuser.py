#1 Please write a program which asks for the user's name and then prints it twice, on two consecutive lines.
#An example of the how the program should function:
#Sample output
#What is your name? Paul
#Paul
#Paul
# Write your solution here
print('Exercicio 1')
name = input("What is your name? ")
print(name)
print(name)

#2 Please write a program which asks for the user's name and then prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, another between the two names and a third one at the end of the line.
#The program should function as follows:
#Sample output
#What is your name? Paul
#!Paul!Paul!
# Write your solution here
print('Exercicio 2')
name = input("What is your name? ")
print("!" + name + "!" + name + "!")

#3 Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:
#Sample output
#Given name: Steve
#Family name: Sanders
#Street address: 91 Station Road
#City and postal code: London EC05 6AW
#Steve Sanders
#91 Station Road
#London EC05 6AW
# Write your solution here
print('Exercicio 3')
givenName = input("Given name: ")
familyName = input("Family name: ")
streetAdress = input("Street adress: ")
cityAndPostalCode = input("City and postal code: ")

print(givenName + " " + familyName)
print(streetAdress)
print(cityAndPostalCode)

#4 Here is a program which should ask for three utterances and print them out, like so:
#Sample output
#The 1st part: hickory
#The 2nd part: dickory
#The 3rd part: dock
#hickory-dickory-dock!
# Fix the code
print('Exercicio 4')
part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + "-" + part2 + "-" + part3 + "!")

#5 Please write a program which prints out the following story. The user gives a name and a year, which should be inserted into the printout.
#Sample output
#Please type in a name: Mary
#Please type in a year: 1572
#Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.
#The story should change according to the input given by the user.
# Write your solution here
print('Exercicio 5')
name = input("Please type in a name: ")
year = input("Please type in a year: ")

print(name + " is a valiant knight, born in the year " + year + ". One morning " + name + " woke up to an awful racket: a dragon was approaching the village. Only " + name + " could save the village's residents.")
