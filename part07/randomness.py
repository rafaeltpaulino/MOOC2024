'''
Please write a function named lottery_numbers(amount: int, lower: int, upper: int), which generates as many random numbers as specified by the first argument. All numbers should fall within the bounds lower to upper. The numbers should be stored in a list and returned. The numbers should be in ascending order in the returned list.

As these are lottery numbers, no number should appear twice in the list.

An example of how the function should work:

for number in lottery_numbers(7, 1, 40):
    print(number)

Sample output

4
7
11
16
22
29
38
'''
# Write your solution here
from random import *

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    temp = list(range(lower, upper))
    res = sample(temp, amount)
    
    return sorted(res)

if __name__ == '__main__':
    print('Exercício 1')
    numbers = lottery_numbers(7, 1, 255)
    print(numbers)
    
'''
Please write a function which creates passwords of a desired length, consisting of lowercase characters a to z.

An example of how the function should work:

for i in range(10):
    print(generate_password(8))

Sample output

lttehepy
olsxttjl
cbjncrzo
dwxqjdgu
gpfdcecs
jabyvgar
xnbbonbl
ktmsjyww
ejhprmel
rjkoacib
'''
# Write your solution here
import string
from random import *

def generate_password(lenght : int) -> str:
    password = ''.join(choice(string.ascii_lowercase) for i in range(lenght))
    
    return password

if __name__ == '__main__':
    print('Exercício 2')
    print(generate_password(8))
    
'''
Please write an improved version of your password generator. The function now takes three arguments:

    If the second argument is True, the generated password should also contain one or more numbers.
    If the third argument is True, the generated password should also contain one or more of these special characters: !?=+-()#.

Despite these two additional arguments, the password should always contain at least one lowercase alphabet. You may assume the function will only be called with combinations of arguments that are possible to formulate into passwords following these rules. That is, the arguments will not specify e.g. a password of length 2 which contains both a number and a special characters, for then there would not be space for the mandatory lowercase letter.

An example of how the function should work:

for i in range(10):
    print(generate_strong_password(8, True, True))

Sample output

2?0n+u31
u=m4nl94
n#=i6r#(
da9?zvm?
7h)!)g?!
a=59x2n5
(jr6n3b5
9n(4i+2!
32+qba#=
n?b0a7ey
'''
# Write your solution here
import string
from random import *

def generate_strong_password(lenght : int, numbers : bool, special_chars : bool) -> str:
    password = ''
    certainty = randint(0, (lenght // 2) - 1)
    certainty2 = randint(lenght // 2, lenght - 1)
    
    while len(password) < lenght:
        if certainty == len(password) and numbers == True:
            password += choice(string.digits)
            
        if certainty2 == len(password) and special_chars == True:
            password += choice('!?=+-()#')
        else:    
            password += choice(string.ascii_lowercase)
            
    return password
            
if __name__ == '__main__':
    print('Exercício 3')
    print(generate_strong_password(5, True, True))