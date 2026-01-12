'''
Please write a function named read_input, which asks the user for input until the user types in an integer which falls within the bounds given as arguments to the function. The function should return the final valid integer value typed in by the user.

An example of the function in action:

number = read_input("Please type in a number: ", 5, 10)
print("You typed in:", number)

Sample output

Please type in a number: seven
You must type in an integer between 5 and 10
Please type in a number: -3
You must type in an integer between 5 and 10
Please type in a number: 8
You typed in: 8
'''
# Write your solution here
def read_input(message : str, min : int, max : int) -> int:
    while True:
        try:
            num = int(input(message))
            
            if num >= min and num <= max:
                return num
            
        except ValueError:
            pass
        
        print(f'You must type in an integer between {min} and {max}')
        
if __name__ == '__main__':
    print('Exercício 1')
    num = read_input("Please type in a number: ", 5, 10)
    print(f'You typed in: {num}')
    
'''
Please write a function named new_person(name: str, age: int), which creates and returns a tuple containing the data in the arguments. The first element should be the name and the second the age.

If the values stored in the parameter variables are not valid, the function should throw a ValueError exception.

Invalid parameters in this case include:

    name is an empty string
    name contains less than two words
    name is longer than 40 characters
    age is a negative number
    age is greater than 150
'''
# Write your solution here
def new_person(name: str, age: int) -> tuple:
    if name == '':
        raise ValueError('Error: Name cannot be empty')
    
    if len(name.split(' ')) < 2:
        raise ValueError('Error: Name has to be at least 2 words')
    
    if len(name) > 40:
        raise ValueError('Error: Name is longer than 40 characters')
    
    if age < 0:
        raise ValueError('Error: Age cannot be negative')
    
    if age > 150:
        raise ValueError('Error: Age cannot be greater than 150')
    
    return name, age

if __name__ == '__main__':
    print('Exercício 2')
    try:
        person = new_person('rafael', 26)
        print(person)
    except:
        print('Invalid input')
    
'''
The file lottery_numbers.csv containts winning lottery numbers in the following format:
Sample data

week 1;5,7,11,13,23,24,30
week 2;9,13,14,24,34,35,37
...etc...

Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.

The file has been corrupted. Lines in the file may contain the following kinds of errors (these exact lines may not be present in the file, but errors in a similar format will be):

The week number is incorrect:
Sample data

week zzc;1,5,13,22,24,25,26

One or more numbers are not correct:
Sample data

week 22;1,**,5,6,13,2b,34

Too few numbers:
Sample data

week 13;4,6,17,19,24,33

The numbers are too small or large:
Sample data

week 39;5,9,15,35,39,41,105

The same number appears twice:
Sample data

week 41;5,12,3,35,12,14,36

Please write a function named filter_incorrect(), which creates a file called correct_numbers.csv. The file should contain only those lines from the original file which are in the correct format.
'''
# Write your solution here
def readFile() -> dict:
    res = {}
        
    with open('lottery_numbers.csv') as lotteryNumbers:
        for line in lotteryNumbers:
            line = line.replace('\n', '')
            temp = line.split(';')
            week = temp[0].split(' ')
            numbers = temp[1].split(',')
            
            res[week[1]] = numbers
            
    return res

def filter_incorrect():
    lotteryNumbers = readFile()
    
    with open('correct_numbers.csv', 'w') as correct:
        for weeks, numbers in lotteryNumbers.items():
            tempNum = ''
            
            try:
                if not weeks.isnumeric():
                    raise ValueError('Invalid week')
                
                if len(numbers) < 7:
                    raise ValueError('Too few numbers')
                
                if len(set(numbers)) < 7:
                    raise ValueError('Number appears twice')
                
                for number in numbers:
                    if not number.isnumeric() or (int(number) <1 or int(number) > 39):
                        raise ValueError('Invalid number')
                    
                    tempNum += f'{number},'
                    
                tempNum = tempNum[:-1]
                tempEntry = f'week {weeks};{tempNum}\n'
                correct.write(tempEntry)
                    
            except ValueError:
                pass
            
if __name__ == '__main__':
    filter_incorrect()