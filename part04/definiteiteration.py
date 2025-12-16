'''
1 Please write a program which asks the user to type in a string. The program then prints each input character on a separate line. After each character there should be a star (*) printed on its own line.

This is how it should work:
Sample output

Please type in a string: Python
P
*
y
*
t 
*
h
*
o
*
n
*

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
# Write your solution here
print('Exercício 1')
userInput = input('Please type in a string: ')

for character in userInput:
    print(character)
    print('*')
    
'''
2 Please write a program which asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, but leaves out the number 0. Each number should be printed on a separate line.

An example of expected behaviour:
Sample output

Please type in a positive integer: 4
-4
-3
-2
-1
1
2
3
4

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
# Write your solution here
print('Exercício 2')
num = int(input('Please type in a positive integer: '))

for i in range(-num, num + 1):
    if(i == 0):
        continue
    
    print(i)

'''
3 Please write a function named list_of_stars, which takes a list of integers as its argument. The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:
Sample output

***
*******
*
*
**
'''
# Write your solution here
def list_of_stars(intList : list):
    for item in intList:
        print('*' * item)
        
if __name__ == '__main__':
    print('Exercício 3')
    myList = [5, 6, 1, 2, 4]
    list_of_stars(myList)
    print()
    myList = [3, 7, 1, 1, 2]
    list_of_stars(myList)
    
'''
4 Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False

Hint: the function sorted can be used on strings as well.
'''
# Write your solution here
def anagrams(word1 : str, word2: str) -> bool:
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

if __name__ == '__main__':
    print('Exercício 4')
    print(anagrams('python', 'java'))
    print(anagrams('arara', 'raraa'))
    print(anagrams('meta', 'tame'))
    print(anagrams('tabby', 'batty'))
    
'''
5 Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.

Please also write a main program which asks the user to type in words until they type in a palindrome:
Sample output

Please type in a palindrome: python
that wasn't a palindrome
Please type in a palindrome: java
that wasn't a palindrome
Please type in a palindrome: oddoreven
that wasn't a palindrome
Please type in a palindrome: neveroddoreven
neveroddoreven is a palindrome!

NB:, the main program should not be within an if __name__ == "__main__": block
'''
# Write your solution here
def palindromes(word : str) -> bool:
    i = -1
    
    for j in range(0, len(word)//2):
        if word[j] != word[i]:
            print("that wasn't a palindrome")
            return False
        
        i -= 1
    
    print(f"{word} is a palindrome!")    
    return True
    
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
print('Exercício 5')
while True:
    word = input('Please type in a palindrome: ')
    
    if palindromes(word):
        break

'''
6 Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)

Sample output

The result is 9
'''
# Write your solution here
def sum_of_positives(intList : list) -> int:
    res = 0
    for number in intList:
        if number > 0:
            res += number
            
    return res

if __name__ == '__main__':
    print('Exercício 6')
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print(f"The result is {result}")
    
'''
7 Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)

Sample output

original [1, 2, 3, 4, 5]
new [2, 4]
'''
# Write your solution here
def even_numbers(intList : list) -> list:
    return [item for item in intList if item % 2 == 0]

if __name__ == "__main__":
    print('Exercício 7')
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
    
'''
8 Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items.

An example of the function at work:

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]
'''
# Write your solution here
def list_sum(intList1 : list, intList2 : list) -> list:
    res = []
    
    for i in range(len(intList1)):
        res.append(intList1[i] + intList2[i])
        
    return res

if __name__ == '__main__':
    print('Exercício 8')
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
    
'''
9 Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.

my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]
'''
# Write your solution here
def distinct_numbers(intList : list) -> list:
    res = []
    
    for item in intList:
        if item not in res:
            res.append(item)
    
    return sorted(res)

if __name__ == '__main__':
    print('Exercício 9')
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
    
'''
10 Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.

my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)

Sample output

8
7
'''
# Write your solution here
def length_of_longest(strList : list) -> int:
    res = len(strList[0])
    
    for item in strList:
        if len(item) > res:
            res = len(item)
            
    return res 

if __name__ == '__main__':
    rprint('Exercício 10')
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
    
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)

'''
11 Please write a function named shortest, which takes a list of strings as its argument. The function returns whichever of the strings is the shortest. If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests). You may assume there will be no empty strings in the list.

my_list = ["first", "second", "fourth", "eleventh"]

result = shortest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = shortest(my_list)
print(result)

Sample output

first
tim
'''
# Write your solution here
def shortest(strList : list) -> str:
    res = strList[0]
    
    for item in strList:
        if len(item) < len(res):
            res = item
            
    return res

if __name__ == '__main__':
    print('Exercício 11')
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)
    
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)
     
'''
12 Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new list containing the longest string in the original list. If more than one are equally long, the function should return all of the longest strings.

The order of the strings in the returned list should be the same as in the original.

my_list = ["first", "second", "fourth", "eleventh"]

result = all_the_longest(my_list)
print(result) # ['eleventh']

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']
'''
# Write your solution here
def all_the_longest(strList : list) -> list:
    longestLenght = length_of_longest(strList)
    res = []
    
    for item in strList:
        if len(item) == longestLenght:
            res.append(item)
            
    return res

if __name__ == '__main__':
    print('Exercício 12')
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']
    
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']