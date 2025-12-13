'''
1 Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again. This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.

An example execution of the program:
Sample output

Index: 0
New value: 10
[10, 2, 3, 4, 5]
Index: 2
New value: 250
[10, 2, 250, 4, 5]
Index: 4
New value: -45
[10, 2, 250, 4, -45]
Index: -1

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
# Write your solution here
print('Exercício 1')
myList = [1, 2, 3, 4, 5]
index = int(input('Index: '))

while index != -1:
    newValue = int(input('New value: '))
    myList[index] = newValue
    print(myList)
    index = int(input('Index: '))
    
'''
2 Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. Finally, the list is printed out.

An example of expected behaviour:
Sample output

How many items: 3
Item 1: 10
Item 2: 250
Item 3: 34
[10, 250, 34]

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
# Write your solution here
print('Exercício 2')
amountItems = int(input('How many items: '))
i = 0
myList = []

while i < amountItems:
    item = int(input(f'Item {i}: '))
    myList.append(item)
    i += 1
    
print(myList)

'''
3 Please write a program which asks the user to choose between addition and removal. Depending on the choice, the program adds an item to or removes an item from the end of a list. The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.

The list is printed out in the beginning and after each operation. Have a look at the example execution below:
Sample output

The list is now []
a(d)d, (r)emove or e(x)it: d
The list is now [1]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2, 3]
a(d)d, (r)emove or e(x)it: r
The list is now [1, 2]
a(d)d, (r)emove or e(x)it: d
The list is now [1, 2, 3]
a(d)d, (r)emove or e(x)it: x
Bye!

You may assume that, if the list is empty, there will not be an attempt to remove items.

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
# Write your solution here
print('Exercício 3')
myList = []
number = 1

while True:
    print(f'The list is now {myList}')
    userChoice = input('a(d)d, (r)emove or e(x)it: ')
    
    if userChoice == 'x':
        print('Bye!')
        break
    
    if userChoice == 'd':
        myList.append(number)
        number += 1
        
    if userChoice == 'r':
        myList.pop(-1)
        number -= 1
        
'''
4 Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.
Sample output

Word: once
Word: upon
Word: a
Word: time
Word: upon
You typed in 4 different words

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
# Write your solution here
print('Exercício 4')
words = []

while True:
    word = input('Word: ')
    
    if word in words:
        break
    else:
        words.append(word)
        
print(f'You typed in {len(words)} different words')

'''
5 Please write a program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:

    in the order the items were added
    ordered from smallest to greatest

The program exits when the user types in 0.

An example of expected behaviour:
Sample output

New item: 3
The list now: [3]
The list in order: [3]
New item: 1
The list now: [3, 1]
The list in order: [1, 3]
New item: 9
The list now: [3, 1, 9]
The list in order: [1, 3, 9]
New item: 5
The list now: [3, 1, 9, 5]
The list in order: [1, 3, 5, 9]
New item: 0
Bye!

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
print('Exercício 5')
# Write your solution here
originalList = []
newItem = int(input('New item: '))

while newItem != 0:
    originalList.append(newItem)
    
    print(f'The list now: {originalList}')
    print(f'The list in order: {sorted(originalList)}')
    
    newItem = int(input('New item: '))
    
print('Bye!')

'''
6 Please write a function named length which takes a list as its argument and returns the length of the list.

my_list = [1, 2, 3, 4, 5]
result = length(my_list)
print("The length is", result)

# the list given as an argument doesn't need to be stored in any variable
result = length([1, 1, 1, 1])
print("The length is", result)

Sample output

The length is 5
The length is 4
'''
# Write your solution here
print('Exercício 6')
def length(userList : list) -> int:
    return len(userList)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)
    my_list = [3, 6, -4, 2, 5, 0, 9, 8]
    result = length(my_list)
    print(result)
    
'''
7 Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.

my_list = [1, 2, 3, 4, 5]
result = mean(my_list))
print("mean value is", result)

Sample output

mean value is 3.0
'''
# Write your solution here
def mean(userList : list) -> float:
    return (sum(userList) / len(userList))

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 7')
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
    my_list = [10, 10]
    result = mean(my_list)
    print(result)
    
'''
8 Please write a function named range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.

my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list))
print("The range of the list is", result)

Sample output

The range of the list is 4
'''
# Write your solution here
def range_of_list(userList : list):
    return max(userList) - min(userList)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print('Exercício 8')
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)