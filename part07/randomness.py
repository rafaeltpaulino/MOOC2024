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
    
'''
In this exercise you will write some functions which can be used in games that involve dice.

Instead of normal dice this exercise specifies non-transitive dice. You can read up on these here or watch this video.

You will use three dice:

    Die A has the sides 3, 3, 3, 3, 3, 6
    Die B has the sides 2, 2, 2, 5, 5, 5
    Die C has the sides 1, 4, 4, 4, 4, 4

Please write a function named roll(die: str), which rolls the die specified by the argument. An example of how this should work:

for i in range(20):
    print(roll("A"), " ", end="")
print()
for i in range(20):
    print(roll("B"), " ", end="")
print()
for i in range(20):
    print(roll("C"), " ", end="")

Sample output

3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  6  3  6  3
2  2  5  2  2  5  5  2  2  5  2  5  5  5  2  5  2  2  2  2
4  4  4  4  4  1  1  4  4  4  1  4  4  4  4  4  4  4  4  4

Also write a function named play(die1: str, die2: str, times: int), which throws both dice as many times as specified by the third argument. The function should return a tuple. The first item should be the number of times die 1 won, the second the number of times die 2 won, and the third item should be the number of ties.

result = play("A", "C", 1000)
print(result)
result = play("B", "B", 1000)
print(result)

Sample output

(292, 708, 0)
(249, 273, 478)
'''
# Write your solution here
from random import *

def roll(die : str) -> int:
    dieA = (3, 3, 3, 3, 3, 6)
    dieB = (2, 2, 2, 5, 5, 5)
    dieC = (1, 4, 4, 4, 4, 4)
    
    if die.lower() == 'a':
        return choice(dieA)
    elif die.lower() == 'b':
        return choice(dieB)
    else:
        return choice(dieC)

def play(die1 : str, die2 : str, times : int) -> tuple:
    die1Wins = 0
    die2Wins = 0
    ties = 0
    
    for i in range(times):
        tempDie1 = roll(die1)
        tempDie2 = roll(die2)
        
        if tempDie1 > tempDie2:
            die1Wins += 1
        elif tempDie2 > tempDie1:
            die2Wins += 1
        else:
            ties += 1
            
    return (die1Wins, die2Wins, ties) 
        
    
if __name__ == '__main__':
    print('Exercício 4')
    temp1 = play('A', 'B', 50)
    temp2 = play('B', 'C', 50)
    temp3 = play('A', 'C', 50)
    
    print(f'Die A vs Die B')
    print(f'Die A wins = {temp1[0]} Die B wins = {temp1[1]} Ties = {temp1[2]}')
    
    print(f'Die B vs Die C')
    print(f'Die B wins = {temp2[0]} Die C wins = {temp2[1]} Ties = {temp2[2]}')
    
    print(f'Die A vs Die C')
    print(f'Die A wins = {temp3[0]} Die C wins = {temp3[1]} Ties = {temp3[2]}')
    
'''
The exercise template contains the file words.txt, which contains some English language words, one on each line.

Please write a function named words(n: int, beginning: str), which returns a list containing n random words from the words.txt file. All words should begin with the string specified by the second argument.

The same word should not appear twice in the list. If there are not enough words beginning with the specified string, the function should raise a ValueError exception.

An example of the function in action:

word_list = words(3, "ca")
for word in word_list:
    print(word)

Sample output

cat
car
carbon
'''
# Write your solution here
from random import *

def ReadFile() -> list:
    res = []
    
    with open('words.txt') as words:
        for word in words:
            temp = word.strip()
            
            res.append(temp)
            
    return res

def words(n : int, beginning : str) -> list:
    wordsFile = ReadFile()
    res = []
    
    for word in wordsFile:
        if word.startswith(beginning):
            res.append(word)
            
    if len(res) < n:
        raise ValueError(f'Number of words with the suffix {beginning} smaller than requested number of words ({n})')
    else:
        shuffle(res)
        return res[0:n]
    
    
if __name__ == '__main__':
    print('Exercício 5')
    word_list = words(3, "calico")
    for word in word_list:
        print(word)