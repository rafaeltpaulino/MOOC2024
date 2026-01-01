'''
Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary. The keys of the dictionary should be the numbers between start_index and end_index inclusive

The value mapped to each key should be the key times ten.

For example:

d = times_ten(3, 6)
print(d)

Sample output

{3: 30, 4: 40, 5: 50, 6: 60}
'''
# Write your solution here
def times_ten(start_index: int, end_index: int) -> dict:
    res = {}
    
    for i in range(start_index, end_index+1):
        res[i] = i * 10
        
    return res 

    
if __name__ == '__main__':
    print('Exercício 1')
    d = times_ten(3, 6)
    print(d)
    
'''
Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.

A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself. For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

An example of the function in action:

k = factorials(5)
print(k[1])
print(k[3])
print(k[5])

Sample output

1
6
120
'''
# Write your solution here
def factorials(n: int) -> dict:
    res = {}
    
    for i in range(1, n+1):
        temp = 1
        for j in range(1, i+1):
            temp *= j
        
        res[i] = temp
        
    return res

if __name__ == '__main__':
    print('Exercício 2')
    k = factorials(10)
    print(k)
    
'''
Please write a function named histogram, which takes a string as its argument. The function should print out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.

For example, the function call histogram("abba") should print out
Sample output

a **
b **

while histogram("statistically") should print out
Sample output

s **
t ***
a **
i **
c *
l **
y *
'''
# Write your solution here
def histogram(word : str):
    temp = {}
    
    for letter in word:
        if letter not in temp:
            temp[letter] = ''
            
        temp[letter] += '*'
        
    for k, v in temp.items():
        print(f'{k} {v}')
        
if __name__ == '__main__':
    print('Exercício 3')
    histogram('statistically')

'''
Please write a phone book application. It should work as follows:
Sample output

command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!
command (1 search, 2 add, 3 quit): 2
name: emily
number: 045-1212344
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
command (1 search, 2 add, 3 quit): 1
name: mary
no number
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...

As you can see above, each name can be attached to a single number only. If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
# Write your solution here
phoneBook = {}
while(True):
    print('Exercício 4')
    option = input('command (1 search, 2 add, 3 quit): ')
    
    match option:
        case '1':
            name = input('name: ')
            
            if name not in phoneBook:
                print('no number')    
            else:
                print(f'{phoneBook[name]}')
                
        case '2':
            name = input('name: ')
            number = input('number: ')
            
            phoneBook[name] = number
            print('ok!')
            
        case '3':
            print('quitting...')
            break
        
        case _:
            print('invalid option')
            
'''
Please write an improved version of the phone book application. Each entry should now accommodate multiple phone numbers. The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.
Sample output

command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!
command (1 search, 2 add, 3 quit): 2
name: emily
number: 045-1212344
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
command (1 search, 2 add, 3 quit): 1
name: mary
no number
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...
'''
# Write your solution here
def add(phoneBook : dict):
    name = input('name:')
    number = input('number:')
    
    if name not in phoneBook:
        phoneBook[name] = []
    
    phoneBook[name].append(number)
    
    print('ok!')
    
def search(phoneBook : dict):
    name = input('name:')
    
    if name not in phoneBook:
        print('no number')
    else:
        for number in phoneBook[name]:
            print(f'{number}')
            
def main():
    print('Exercício 5')
    phoneBook = {}
    
    while True:
        option = input('command (1 search, 2 add, 3 quit): ')
        
        match option:
            case '1':
                search(phoneBook)
                
            case '2':
                add(phoneBook)
                
            case '3':
                print('quitting...')
                break
            
            case _:
                print('invalid option')
                
main()

'''
Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. The dictionary should be inverted in place so that values become keys and keys become values.

An example of its use:

s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)

Sample output

{"first": 1, "second": 2, "third": 3, "fourth": 4}

NB: the principles regarding lists covered here also hold for dictionaries passed as arguments.

If you have trouble completing this exercise, the visualisation tool might help you understand what your code is or isn't doing.
'''
# Write your solution here
def invert(dictionary: dict):
    temp = {}
    
    for k, v in dictionary.items():
        temp[v] = k
        
    dictionary.clear()
    
    for k, v in temp.items():
        dictionary[k] = v
        
    
if __name__ == '__main__':
    print('Exercício 6')
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
    
'''
Please write a function named dict_of_numbers(), which returns a new dictionary. The dictionary should have the numbers from 0 to 99 as its keys. The value attached to each key should be the number spelled out in words. Please have a look at the example below:

numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
print(numbers[45])
print(numbers[99])
print(numbers[0])

Sample output

two
eleven
forty-five
ninety-nine
zero

NB: Please don't formulate each spelled out number by hand. Figure out how you can use loops and dictionaries in your solution.
'''
# Write your solution here
def dict_of_numbers() -> dict:
    helper = {0: 'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 
              14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 
              70:'seventy', 80:'eighty', 90:'ninety'}
    
    for i in range(20, 100):
        if i % 10 == 0:
            temp = 1
            continue
        elif i < 30:
            helper[i] = helper[20] + '-' + helper[temp]
            temp += 1
        elif i < 40:
            helper[i] = helper[30] + '-' + helper[temp]
            temp += 1
        elif i < 50:
            helper[i] = helper[40] + '-' + helper[temp]
            temp += 1    
        elif i < 60:
            helper[i] = helper[50] + '-' + helper[temp]
            temp += 1    
        elif i < 70:
            helper[i] = helper[60] + '-' + helper[temp]
            temp += 1    
        elif i < 80:
            helper[i] = helper[70] + '-' + helper[temp]
            temp += 1    
        elif i < 90:
            helper[i] = helper[80] + '-' + helper[temp]
            temp += 1
        elif i < 100:
            helper[i] = helper[90] + '-' + helper[temp]
            temp += 1
            
    return helper
            
if __name__ == '__main__':
    print('Exercício 7')
    numbers = dict_of_numbers()
    print(numbers)
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
    
'''
Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.

The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys.

    name
    director
    year
    runtime

The values attached to these keys are given as arguments to the function.

An example of its use:

database = []
add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
print(database)

Sample output

[{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]
'''
# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    database.append({
        'name': name,
        'director': director,
        'year': year,
        'runtime': runtime
    })
    
if __name__ == '__main__':
    print('Exercício 8')
    database = []
    add_movie(database, 'Despertar dos Mortos', 'George A. Romero', 1978, 127)
    print(database)
    add_movie(database, 'Eles Vivem', 'John Carpenter', 1988, 93)
    print(database)
    
'''
Please write a function named find_movies(database: list, search_term: str), which processes the movie database created in the previous exercise. The function should formulate a new list, which contains only the movies whose title includes the word searched for. Capitalisation is irrelevant here. A search for ana should return a list containing both Anaconda and Management.

An example of its use:

database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
{"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
{"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

my_movies = find_movies(database, "python")
print(my_movies)

Sample output

[{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]
'''
def find_movies(database: list, search_term: str) -> list:
    moviesFound = []
    
    for movie in database:
        if search_term.lower() in movie['name'].lower():
            moviesFound.append(movie)
            
    return moviesFound
            
    
if __name__ == '__main__':
    print('Exercício 9')
    database = []
    add_movie(database, 'Despertar dos Mortos', 'George A. Romero', 1978, 127)
    add_movie(database, 'Eles Vivem', 'John Carpenter', 1988, 93)
    add_movie(database, 'Madrugada dos Mortos', 'Zack Snyder', 2004, 103)
    
    my_movies = find_movies(database, "mortos")
    print(my_movies)