'''
Please write a function named hypotenuse(leg1: float, leg2: float), which takes the lengths of the two sides adjacent to the right angle of an orthogonal triangle. The function should return the length of the hypotenuse, or the side opposite to the right angle.

You can use the Pythagorean theorem to calculate the result. You will need the sqrt function from the math module.

Some examples:

print(hypotenuse(3,4)) # 5.0
print(hypotenuse(5,12)) # 13.0
print(hypotenuse(1,1)) # 1.4142135623730951
'''
# Write your solution here
from math import sqrt

def square(x: float) -> float:
    return x * x

def hypotenuse(leg1: float, leg2: float) -> float:
    return sqrt(square(leg1) + square(leg2))

if __name__ == '__main__':
    print('Exercício 1')
    print(hypotenuse(1, 1))
    
'''
The Python module string contains some string constants, which define certain groups of characters. These include for example lowercase letters and punctuation characters. Please familiarize yourself with these constants, and then write a function named separate_characters(my_string: str). The function takes a string as its argument, and it should separate the characters in the string into three other strings, and return these in a tuple:

    The first string should contain the lowercase and uppercase ASCII letters (string constant ascii_letters)
    The second string should contain all punctuation characters defined by the string constant punctuation
    The third string should contain all the other characters (including whitespace)

The characters should appear in the three strings in the same order as they appeared in the original string.

An example of the function in action:

parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])
print(parts[1])
print(parts[2])

Sample output

OlHeyaremltswrking
!!!,?
é  üäü ö
'''
# Write your solution here
import string

def separate_characters(my_string: str) -> tuple:
    normalLetters = ''
    rest = ''
    punct = ''
    
    for character in my_string:
        if character in string.ascii_letters:
            normalLetters += character
        elif character in string.punctuation:
            punct += character
        else:
            rest += character
            
    return normalLetters, punct, rest

if __name__ == '__main__':
    print('Exercício 2')
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
    
'''
Please familiarize yourself with the Python module fractions. Use it to write a function named fractionate(amount: int), which takes the number of parts as its argument. The function should divide the number 1 into as many equal sized fractions as is specified by the argument, and return these in a list.

An example of the function in action:

for p in fractionate(3):
    print(p)

print()

print(fractionate(5))

Sample output

1/3
1/3
1/3

[Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5)]
'''
# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    res = []
    
    for i in range(amount):
        res.append(Fraction(1, amount))
        
    return res

if __name__ == '__main__':
    print('Exercício 3')
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))