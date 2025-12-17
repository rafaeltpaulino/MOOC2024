'''
1 Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.

An example of how the function should work:

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)

Sample output

['erom eno', 'elpmaxe', 'ereht', 'iH']
'''
# Write your solution here      
def everything_reversed(strList : list[str]) -> list[str]:
    res = []
    
    for i in range(-1, -len(strList)- 1, -1):
        res.append(strList[i][::-1])
        
    return res

if __name__ == '__main__':
    print('Exercício 1')
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
    
'''
2 Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

An example of expected behaviour:

first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))

Sample output

b
e
'''
# Write your solution here
def most_common_character(string : str) -> str:
    index = 0
    
    for i in range(1, len(string), 1):
        if (string.count(string[i])) > (string.count(string[index])):
            index = i
    
    return string[index]
    
if __name__== '__main__':
    print('Exercício 2')
    first_string = "abcdbde"
    print(most_common_character(first_string))
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
    third_string = "zaza"
    print(most_common_character(third_string))
    
'''
3 Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.

You can assume the string will contain only characters from the lowercase English alphabet a...z.

An example of expected behaviour:

my_string = "this is an example"
print(no_vowels(my_string))

Sample output

ths s n xmpl
'''
# Write your solution here
def no_vowels(string : str) -> str:
    vowels = 'aeiou'
    res = ''
    
    for char in string:
        if char not in vowels:
            res += char
            
    return res 

if __name__ == '__main__':
    print('Exercício 3')
    my_string = "this is an example"
    print(no_vowels(my_string))
    my_string = "rafael"
    print(no_vowels(my_string))
    
'''
4 The Python string method isupper() returns True if a string consists of only uppercase characters.

Some examples:

print("XYZ".isupper())

is_it_upper = "Abc".isupper()
print(is_it_upper)

Sample output

True
False

Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.

An example of expected behaviour:

my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
pruned_list = no_shouting(my_list)
print(pruned_list)

Sample output

['def', 'lower', 'another lower', 'Capitalized']
'''
# Write your solution here
def no_shouting(strList : list[str]) -> list[str]:
    return [item for item in strList if not item.isupper()]

if __name__ == '__main__':
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
    
'''
5 Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.

Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.

For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

An example function call:

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))

Sample output

4
'''
# Write your solution here
def longest_series_of_neighbours(intList : list[int]) -> int:
    res = 0
    
    for i in range(len(intList) - 1):
        j = 0
        k = i
        
        while (intList[k] - intList[k+1] == 1 or intList[k] - intList[k+1] == -1) and k < len(intList) - 1:
            j += 1
            k += 1
            
            if k == len(intList) - 1:
                break
            
        if j > res:
            res = j + 1
            
        i = k
        
    return res

if __name__ == '__main__':
    print('Exercício 5')
    my_list = [1, 3, 5, 7, 15, 5, 60, 3, 44, 12, 0]
    print(longest_series_of_neighbours(my_list))
    
'''
6 In this exercise you will write a program for printing out grade statistics for a university course.

The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. The program then prints out statistics based on the results.

Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.

The program keeps asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.

And example of how the data is typed in:
Sample output

Exam points and exercises completed: 15 87
Exam points and exercises completed: 10 55
Exam points and exercises completed: 11 40
Exam points and exercises completed: 4 17
Exam points and exercises completed:
Statistics:

When the user types in an empty line, the program prints out statistics. They are formulated as follows:

The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point, 20% grants two points, and so forth. Completing all 100 exercises grants 10 exercise points. The number of exercise points granted is an integer value, rounded down.

The grade for the course is determined based on the following table:
exam points + exercise points	grade
0–14	0 (i.e. fail)
15–17	1
18–20	2
21–23	3
24–27	4
28–30	5

There is also an exam cutoff threshold. If a student received less than 10 points from the exam, they automatically fail the course, regardless of their total number of points.

With the example input from above the program would print out the following statistics:
Sample output

Statistics:
Points average: 14.5
Pass percentage: 75.0
Grade distribution:
  5:
  4:
  3: *
  2:
  1: **
  0: *

Floating point numbers should be printed out with one decimal precision.

NB: this exercise doesn't ask you to write any specific functions, so you should not place any code within an if __name__ == "__main__" block. If any functionality in your program is e.g. in the main function, you should include the code calling this function normally, and not contain it in an if block like in the exercises which specify certain functions.

Hint:

The user input in this program consists of lines with two integer values:
Sample output

Exam points and exercises completed: 15 87

You have to first split the input line in two and then convert the sections into integers with the int function. Splitting the input can be achieved in the same way as in the exercise First, second and last words, but there is a simpler way as well. The string method split will chop the input up nicely. You will find more information by searching for python string split online.
'''
# Write your solution here
def user_input() -> list[int]:
    temp = ''
    pointsExercises = input('Exam points and exercises completed: ')
    
    while pointsExercises:
        temp += pointsExercises + ' '
        
        pointsExercises = input('Exam points and exercises completed: ')
        
    res = temp.split()
    
    return list(map(lambda item: int(item), res))

def calculate_exercise_points(examsCompleted : int) -> int:
    return examsCompleted // 10

def calculate_students_points(userInput : list[int]) -> list[int]:
    totalPoints = []
    
    for i in range(0, len(userInput), 2):
        totalPoints.append(userInput[i] + calculate_exercise_points(userInput[i + 1]))
        
    return totalPoints

def get_grades(studentsPoints : list[int], studentSituation : list[int]) -> list[int]:
    grades = [0, 0, 0, 0, 0, 0]
    
    for i in range(len(studentsPoints)):
        if studentSituation[i] != 0:
            if studentsPoints[i] < 15:
                grades[0] += 1        
            elif studentsPoints[i] < 18:
                grades[1] += 1  
            elif studentsPoints[i] < 21:
                grades[2] += 1            
            elif studentsPoints[i] < 24:
                grades[3] += 1  
            elif studentsPoints[i] < 28:
                grades[4] += 1  
            elif studentsPoints[i] < 31:
                grades[5] += 1
        else:
            grades[0] += 1
            
    return grades
            
def calculate_average(sumofElements : int, quantityOfElements : int) -> float:
    return sumofElements / quantityOfElements

def get_student_situation(userInput : list[int], studentsPoints : list[int]) -> list[int]:
    res = []
    j = 0
    
    #1 == APPROVED / 0 == FAILED
    for i in range(0, len(userInput), 2):
        if userInput[i] >= 10 and studentsPoints[j] > 14:
            res.append(1)
        else:
            res.append(0)
            
        j += 1
        
    return res

def print_statistics(userInput : list[int]):
    studentsPoints = calculate_students_points(userInput)
    avgPoints = calculate_average(sum(studentsPoints), len(studentsPoints))
    studentSituation = get_student_situation(userInput, studentsPoints)
    grades = get_grades(studentsPoints, studentSituation)
    
    print('Statistics:')
    print(f'Points average: {avgPoints:.1f}')
    print(f'Pass percentage: {calculate_average(sum(studentSituation), len(studentSituation)) * 100:.1f}')
    print('Grade distribution:')
    for i in range(5, -1, -1):
        print(f'{i}: {'*' * grades[i]}')
    
def main():
    print('Exercício 6')
    userInput = user_input()
    print_statistics(userInput)
    
main()