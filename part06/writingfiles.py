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
    filter_solutions()
    