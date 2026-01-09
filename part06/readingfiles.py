'''
The file numbers.txt contains integer numbers, one number per line. The contents could look like this:

2
45
108
3
-10
1100
...etc...

Please write a function named largest, which reads the file and returns the largest number in the file.

Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.

NB: If Visual Studio Code can't find the file and you have checked that there are no spelling errors, take a look at the instructions following this exercise.
'''
# write your solution here
def largest() -> int:
    res = []
    
    with open('part06/arquivos/numbers.txt') as newFile:
        
        for line in newFile:
            res.append(int(line))
            
    return max(res)
        
if __name__ == '__main__':
    print('Exercício 1')
    print(largest())

'''
The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:

banana;6.50
apple;4.95
orange;8.0
...etc...

Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents. In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.

NB: the function does not take any arguments. The file you are working with is always named fruits.csv.
'''
# write your solution here
def read_fruits():
    res = {}
    
    with open('part06/arquivos/fruits.csv') as fruits:
        for fruit in fruits:
            temp = fruit.split(';')
            res[temp[0]] = float(temp[1])
            
    return res
            
if __name__ == '__main__':
    print('Exercício 2')
    fruits = read_fruits()
    for fruit, price in fruits.items():
        print(f'fruit: {fruit}, price: {price}')
        
'''
The file matrix.txt contains a matrix in the format specified in the example below:

1,0,2,8,2,1,3,2,5,2,2,2
9,2,4,5,2,4,2,4,1,10,4,2
...etc...

Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.

Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. For example, calling row_sums when the matrix in the file is defined as

1,2,3
2,3,4

the function should return the list [6, 9].

Hint: you can also include other helper functions in your program. It is very worthwhile to spend a moment considering which functionalities are shared by the three functions you are asked to write. Notice that the three functions named above do not take any arguments, but any helper functions you write may take arguments. The file you are working with is always named matrix.txt.

NB: If Visual Studio Code can't find the file and you have checked that there are no spelling errors, take a look at the instructions before this exercise.
'''
# write your solution here
def row_sums() -> list[int]:
    sums = []
    
    with open('src/arquivos/matrix.txt') as matrix:
        for row in matrix:
            temp = [int(num) for num in row.split(',')]
            sums.append(sum(temp))
            
    return sums

def matrix_sum() -> int:
    rowSums = row_sums()
    res = 0
    
    for sum in rowSums:
        res += sum

    return res

def matrix_max() -> int:
    res = []
    
    with open('part06/arquivos/matrix.txt') as matrix:
        for row in matrix:
            temp = [int(num) for num in row.split(',')]
            res.append(max(temp))
            
    return max(res)

if __name__ == '__main__':
    print('Exercício 3')
    print(row_sums())
    print(matrix_sum())
    print(matrix_max())
    
'''
This program works with two CSV files. One of them contains information about some students on a course:

id;first;last
12345678;peter;pythons
12345687;jean;javanese
12345699;alice;adder

The other contains the number of exercises each student has completed each week:

id;e1;e2;e3;e4;e5;e6;e7
12345678;4;1;1;4;5;2;4
12345687;3;5;3;1;5;4;6
12345699;10;2;2;7;10;2;2

As you can see above, both CSV files also have a header row, which tells you what each column contains.

Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student. If the files have the contents in the examples above, the program should print out the following:
Sample output

Student information: students1.csv
Exercises completed: exercises1.csv
pekka peloton 21
jaana javanainen 27
liisa virtanen 35

Hint: while testing your program, you may quickly run out of patience if you always have to type in the file names at the prompt. You might want to hard-code the user input, like so:

if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

The actual functionality of the program is now "hidden" in the False branch of an if statement. It will never be executed.

Now, if you want to quickly verify the program works correctly also with user input, you can just replace False with True:


if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

When you have verified your program works correctly, you can remove the if structure, keeping the commands asking for input.

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

NB2: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.
'''    
# write your solution here
def readFile(fileName : str) -> list:
    res = []
    
    with open (fileName) as newFile:
        for line in newFile:
            line = line.strip()
            data = line.split(';')
            if data[0] != 'id':
                res.append(data)
            
        
    return res

def createStudentDict(studentData : list) -> dict:
    students = {}
    
    for student in studentData:
        students[student[0]] = student[1:]
        
    return students

def createGradesDict(gradesData : list) -> dict:
    grades = {}
    
    for entry in gradesData:
        grades[entry[0]] = [int(grade) for grade in entry[1:]]
        
    return grades

def courseGrading(): 
    studentFile = input('Student information: ')
    gradesFile = input('Exercises information: ')
    
    students = createStudentDict(readFile(studentFile))
    grades = createGradesDict(readFile(gradesFile))
    
    for studentID in students:
        if studentID in grades:
            print(f'{students[studentID][0] + ' ' + students[studentID][1]} {sum(grades[studentID])}')

def main():
    print('Exercício 4')           
    courseGrading()
    
main()

'''
Please write a program which asks the user to type in some text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. Please see the two examples below:
Sample output

Write text: We use ptython to make a spell checker

We use *ptython* to make a spell checker

Sample output

Write text: This is acually a good and usefull program

This is *acually* good and *usefull* program

The case of the letters should be irrelevant to the functioning of your program.

The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as correct.

NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

NB2 If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.
'''
# write your solution here
def spell_checker(string : str):
    words = []
    text = string.split()
    
    with open('wordlist.txt') as wordlist:
        for word in wordlist:
            words.append(word.strip().lower())
            
    for word in text:
        if word.lower() not in words:
            string = string.replace(word, f'*{word}*')        
    
    return string
    
def main():
    print('Exercício 7')
    text = input('Write text: ')
    print(spell_checker(text))
    
main()

'''
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

This exercise is about creating a program which allows the user to search for recipes based on their names, preparation times, or ingredients used. The program should read the recipes from a file submitted by the user.

Each recipe consists of three or more lines. The first line has the name of the recipe, the second line contains an integer number representing the preparation time in minutes, and the remaining line or lines contain the ingredients used, one on each line. The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file. So, there can be more than one recipe in a single file, like in the example below.

Pancakes
15
milk
eggs
flour
sugar
salt
butter

Meatballs
45
mince
eggs
breadcrumbs

Tofu rolls
30
tofu
rice
water
carrot
cucumber
avocado
wasabi

Cake pops
60
milk
bicarbonate
eggs
salt
sugar
cardamom
butter

Hint: it might be best to first read through all the lines in the file and pop them into a list, which is then easier to manipulate in the way described in the exercise.
Search for recipes based on the name of the recipe

Please write a function named search_by_name(filename: str, word: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose name contains the given search string. The names of these recipes are then returned in a list.

An example of the function in action:

found_recipes = search_by_name("recipes1.txt", "cake")

for recipe in found_recipes:
    print(recipe)

Sample output

Pancakes
Cake pops

As you can see in the example above, the case of the letters is irrelevant. The search term cake returns both Pancakes and Cake pops, even though the latter is capitalized.

NB: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.
Search for recipes based on the preparation time

Please write a function named search_by_time(filename: str, prep_time: int), which takes a filename and an integer as its arguments. The function should go through the file and select all recipes whose preparation time is at most the number given.

The names of these recipes are again returned in a list, but the preparation time should be appended to each name. Please have a look at the example below.

found_recipes = search_by_time("recipes1.txt", 20)

for recipe in found_recipes:
    print(recipe)

Sample output

Pancakes, preparation time 15 min
Search for recipes based on the ingredients

A word of caution: this third part of the exercise is considerably more demanding than the previous two. If you feel like you aren't making headway, it may be worth your while to move on, complete the other exercises in this part of the material, and then come back to this exercise if you have time later. Remember, you can submit and receive points for the first two parts of this exercise even if you haven't completed the third part.

Please write a function named search_by_ingredient(filename: str, ingredient: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose ingredients contain the given search string.

The names of these recipes are returned in a list just like in the second part, with the preparation time appended. Please have a look at the example below.

found_recipes = search_by_ingredient("recipes1.txt", "eggs")

for recipe in found_recipes:
    print(recipe)

Sample output

Pancakes, preparation time 15 min
Meatballs, preparation time 45 min
Cake pops, preparation time 60 min
'''
# Write your solution here
def readRecipesFile(fileName : str) -> list:
    fileData = []
    
    with open(fileName) as file:
        for line in file:
            fileData.append(line.strip())
    
    recipe = []
    recipes = []
    
    for i in range(0, len(fileData)):
        if fileData[i] == '':
            recipes.append(recipe)
            recipe = []
        elif i == len(fileData) - 1:
            recipe.append(fileData[i])    
            recipes.append(recipe)
        else:
            recipe.append(fileData[i])       
                 
    return recipes

def search_by_name(filename: str, word: str) -> list:
    recipes = readRecipesFile(filename)
    res = []
    
    for recipe in recipes:
        if word.lower() in recipe[0].lower():
            res.append(recipe[0])
            
    return res

def search_by_time(filename: str, prep_time: int) -> list:
    recipes = readRecipesFile(filename)
    res = []
    
    for recipe in recipes:
        if prep_time >= int(recipe[1]):
            res.append(f'{recipe[0]}, preparation time {recipe[1]} min')
            
    return res

def search_by_ingredient(filename: str, ingredient: str) -> list:
    recipes = readRecipesFile(filename)
    res = []
    
    for recipe in recipes:
        if ingredient in recipe:
            res.append(f'{recipe[0]}, preparation time {recipe[1]} min')
            
    return res
    
if __name__ == '__main__':
    print('Exercício 8')
    name = search_by_name('recipes1.txt', 'a')
    prepTime = search_by_time('recipes1.txt', 20)
    ingredients = search_by_ingredient('recipes1.txt', 'eggs')
    print(f'Search by name: {name}')
    print(f'Search by prep time: {prepTime}')
    print(f'Search by ingredient: {ingredients}')
    

'''
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

In this exercise we will write some functions for working on a file containing location data from the stations for city bikes in Helsinki.

Each file will follow this format:

Longitude;Latitude;FID;name;total_slot;operative;id
24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003

Each station has a single line in the file. The line contains the coordinates, name, and other identifying information for the station.
Distance between stations

First, write a function named get_station_data(filename: str). This function should read the names and locations of all the stations in the file, and return them in a dictionary with the following format:
Sample output

{
  "Kaivopuisto": (24.950292890004903, 60.155444793742276),
  "Laivasillankatu": (24.956347471358754, 60.160959093887129),
  "Kapteeninpuistikko": (24.944927399779715, 60.158189199971673)
}

Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of the station. The first element in the tuple is the Longitude field, and the second is the Latitude field.

Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance between the two stations given as arguments.

The distance is calculated using the Pythagorean theorem. The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.

# we will need the function sqrt from the math module 
import math

x_km = (longitude1 - longitude2) * 55.26
y_km = (latitude1 - latitude2) * 111.2
distance_km = math.sqrt(x_km**2 + y_km**2)

Some examples of the function in action:

stations = get_station_data('stations1.csv')
d = distance(stations, "Designmuseo", "Hietalahdentori")
print(d)
d = distance(stations, "Viiskulma", "Kaivopuisto")
print(d)

Sample output

0.9032737292463177
0.7753594392019532

NB: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.
The greatest distance

Please write a function named greatest_distance(stations: dict), which works out the two stations on the list with the greatest distance from each other. The function should return a tuple, where the first two elements are the names of the two stations, and the third element is the distance between the two.

stations = get_station_data('stations1.csv')
station1, station2, greatest = greatest_distance(stations)
print(station1, station2, greatest)

Sample output

Laivasillankatu Hietalahdentori 1.478708873076181
'''
# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str) -> dict:
    res = {}
    
    with open(filename) as newFile:
        for line in newFile:
            temp = line.split(';')
            
            if temp[0] == 'Longitude':
                continue
            
            res[temp[3]] = (float(temp[0]), float(temp[1]))
            
    return res

def distance(stations: dict, station1: str, station2: str) -> float:
    longitude1 = stations[station1][0]
    latitude1 = stations[station1][1]
    
    longitude2 = stations[station2][0]
    latitude2 = stations[station2][1]
    
    xKm = (longitude1 - longitude2) * 55.26
    yKm = (latitude1 - latitude2) * 111.2
    
    return math.sqrt(xKm**2 + yKm**2)

def greatest_distance(stations: dict) -> tuple:
    greatestDistance = ['', '', 0]
    stationsKeys = list(stations.keys())        
    
    for station in stations:
        for i in range(1, len(stationsKeys)):
            distanceStations = distance(stations, station, stationsKeys[i])
            
            if distanceStations > greatestDistance[2]:
                greatestDistance[0] = station
                greatestDistance[1] = stationsKeys[i]
                greatestDistance[2] = distanceStations
                
    return tuple(greatestDistance)
    
if __name__ == '__main__':
    print('Exercício 9')
    stations = get_station_data('stations2.csv')
    distanceStations = distance(stations, 'Viiskulma', 'Kaivopuisto')
    temp = greatest_distance(stations)
    print(f'Greatest distance: {temp}')