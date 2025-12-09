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