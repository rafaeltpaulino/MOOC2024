'''
Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user. Please see the example below.
Sample output

Whom should I sign this to: Ada
Where shall I save it: inscribed.txt

The contents of the file inscribed.txt would be
Sample data

Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
# Write your solution here
def inscription(name : str, filename : str):
    with open(filename, 'w') as myFile:
        string = f'Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team'
        myFile.write(string)
        
def main():
    print('Exercício 1')
    name = input('Whom should I sign this to: ')
    filename = input('Where shall I save it: ')
    inscription(name, filename)
    
main()

'''
Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. When the program is executed, it should first read any entries already in the file.

NB: the automatic tests for this exercise will change the contents of the file. If you want to keep its contents, first make a copy of the file under a different name.

The program should work as follows:
Sample output

1 - add an entry, 2 - read entries, 0 - quit
Function: 1
Diary entry: Today I ate porridge
Diary saved

1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
1 - add an entry, 2 - read entries, 0 - quit
Function: 1
Diary entry: I went to the sauna in the evening
Diary saved

1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
I went to the sauna in the evening
1 - add an entry, 2 - read entries, 0 - quit
Function: 0
Bye now!

When the program is executed for the second time, this should happen:
Sample output

1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
I went to the sauna in the evening
1 - add an entry, 2 - read entries, 0 - quit
Function: 0
Bye now!

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
# Write your solution here
def addEntry(entry : str):
    with open('diary.txt', 'a') as diary:
        temp = entry + '\n'
        diary.write(temp)
        
    print('Diary saved')
    
def readEntries():
    with open('diary.txt') as diary:
        for entry in diary:
            print(entry.rstrip())
            
def main():
    print('Exercício 2')
    print('1 - add an entry, 2 - read entries, 0 - quit')
    
    while True:
        option = input('Function: ')
        
        match option:
            case '0':
                print('Bye now!')
                break
            case '1':
                entry = input('Diary entry: ')
                addEntry(entry)
            case '2':
                readEntries()
            case _:
                print('invalid option')
        
main()

'''
The file solutions.csv contains some solutions to mathematics problems:

Arto;2+5;7
Pekka;3-2;1
Erkki;9+3;11
Arto;8-3;4
Pekka;5+5;10
...jne...

As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.

Please write a function named filter_solutions() which

    Reads the contents of the file solutions.csv
    writes those lines which have a correct result into the file correct.csv
    writes those lines which have an incorrect result into the file incorrect.csv

Using the example above, the file correct.csv would contain the lines

Arto;2+5;7
Pekka;3-2;1
Pekka;5+5;10

The other two would be in the file incorrect.csv.

Please write the lines in the same order as they appear in the original file. Do not change the original file.

NB: the function should have the exact same result, no matter how many times it is called. That is, it shouldn't matter if the function is called once

filter_solutions()

or multiple times in a row

filter_solutions()
filter_solutions()
filter_solutions()
filter_solutions()

After the execution, the contents of the files correct.csv and incorrect.csv should be exactly the same in either case.
'''
# Write your solution here
def isCorrect(result : int, studentResult : int):
    return result == studentResult

def generateFile(results : list, filename : str):
    with open(filename, 'w') as newFile:
        for entry in results:
            newFile.write(entry) 
    
def filter_solutions():
    correct = []
    incorrect = []
    
    with open('solutions.csv') as solutions:
        for entry in solutions:
            formattedEntry = entry.split(';')
            formattedEntry[2] = formattedEntry[2].strip()
            
            if '+' in formattedEntry[1]:
                temp = formattedEntry[1].split('+')
                result = int(temp[0]) + int((temp[1]))
                check = isCorrect(result, int(formattedEntry[2]))
            else:
                temp = formattedEntry[1].split('-')
                result = int(temp[0]) - int((temp[1]))
                check = isCorrect(result, int(formattedEntry[2]))
            
            if check:
                correct.append(entry)
            else:
                incorrect.append(entry)
                
    generateFile(correct, 'correct.csv')
    generateFile(incorrect, 'incorrect.csv')
          
if __name__ == '__main__':
    print('Exercício 3')
    filter_solutions()


'''
Please write a function named store_personal_data(person: tuple), which takes a tuple containing some identifying information as its argument.

The tuple contains the following elements:

    Name (string)
    Age (integer)
    Height (float)

This should be processed and written into the file people.csv. The file may already contain some data; the new entry goes to the end of the file. The data should be written in the format

name;age;height

Each entry should be on a separate line. If we call the function with the argument ("Paul Paulson", 37, 175.5), the function should write this line to the end of the file:

Paul Paulson;37;175.5
'''
# Write your solution here
def store_personal_data(person: tuple):
    with open('people.csv', 'a') as people:
        temp = ''
        for data in person:
            temp += f'{data};'
        
        temp = temp[:-1]
        temp += '\n'
        
        people.write(temp)
        
if __name__ == '__main__':
    print('Exercicio 4')
    person = ("Paul Paulson", 37, 175.5)
    store_personal_data(person)
    
'''
The exercise template includes the file words.txt, which contains words in English.

Please write a function named find_words(search_term: str). It should return a list containing all the words in the file which match the search term.

The search term may include lowercase letters and the following wildcard characters:

    A dot . means that any single character is acceptable in its place. For example, ca. would yield words like cat and car, p.ng would yield words like ping and pong, and .a.e would yield words like sane, care and late.
    An asterisk * at the end of the search term means that any word which begins with the search term is acceptable. An asterisk at the beginning of the search term means that any word which ends with the search term is acceptable. For example, ca* would yield words like california, cat, caring and catapult, while *ane would yield words like crane, insane and aeroplane. There can only ever be a single asterisk in the search term.
    If there are no wildcard characters in the search term, only words which match the search term exactly are returned.

You may assume both wildcards are never used in the same search term.

The words in the file are all written in lowercase. You may also assume the argument to the function will be in lowercase entirely.

If no matching words are found, the function should return an empty list.

Hint: the Pythons string methods startswith() and endswith() may be useful here. You can search for more information about them online.

An example of the function in action:

print(find_words("*vokes"))

Sample output

['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']
'''
# Write your solution here
import re

def find_words(search_term: str) -> list:
    searchSesult = []
    
    with open('words.txt') as words:
        for word in words:
            temp = word.rstrip()
            
            if search_term == temp:
                searchSesult.append(temp)
            
            if search_term.startswith('*'):
                if temp.endswith(search_term[1:]):
                    searchSesult.append(temp)
                    
            if search_term.endswith('*'):
                if temp.startswith(search_term[:-1]):
                    searchSesult.append(temp)
                        
            if '.' in search_term:
                if len(temp) == len(search_term):
                    temp1 = search_term.replace('.', '\w')
                    match = re.search(temp1, temp)
                        
                    if match != None:
                        searchSesult.append(temp)
                    
    return searchSesult
                    
if __name__ == '__main__':
    print('Exercício 6')
    temp = find_words('.a.e')
    print(temp)
    
'''
Please write a program which functions as a dictionary. The user can type in new entries or look for existing entries.

The program should work as follows:
Sample output

1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: auto
The word in English: car
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: roska
The word in English: garbage
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: laukku
The word in English: bag
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: bag
roska - garbage
laukku - bag
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: car
auto - car
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: laukku
laukku - bag
1 - Add word, 2 - Search, 3 - Quit
Function: 3
Bye!

The dictionary entries should be written to a file called dictionary.txt. The program should first read the contents of the file. New entries are written to the end of the file whenever they are added to the dictionary.

The format of the data stored in the dictionary is up to you.

NB: the automatic tests for this exercise may change the contents of the file. If you want to keep its contents, first make a copy of the file under a different name.

NB2: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
'''
# Write your solution here
# Write your solution here
def generateDict() -> dict:
    res = {}
    
    with open('dictionary.txt') as dictionary:
        for entry in dictionary:
            if entry != '\n':
                temp = entry.split(';')
                temp[1] = temp[1].rstrip()
                
                res[temp[0]] = temp[1]
                
    return res
    
def addWord(word : str, translation : str):
    dictionary = generateDict()
    
    if word in dictionary:
        print(f'{word} already in the dictionary')
    else:
        with open('dictionary.txt', 'a') as dictFile:
            temp = f'{word};{translation + '\n'}'
            dictFile.write(temp)
            
            print('Dictionary entry added')

def searchWord(word : str):
    dictionary = generateDict()
    wordLower = word.lower()
    
    for k, v in dictionary.items():
        if wordLower in k or v:
            print(f'{k} - {v}')
                
def useDictionary():
    while True:
        print('1 - Add word, 2 - Search, 3 - Quit')
        option = input('Function: ')
        
        match option:
            case '1':
                finnishWord = input('The word in Finnish: ')
                translation = input('The word in English: ')
                addWord(finnishWord, translation)
                
            case '2':
                word = input('Search term: ')
                searchWord(word)
                
            case '3':
                print('Bye!')
                return

            case _:
                print('Invalid option.')

def main():
    print('Exercício 7')
    useDictionary()
    
main()