'''
Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:

    The first element in the tuple is the smallest of the arguments
    The second element in the tuple is the greatest of the arguments
    The third element in the tuple is the sum of the arguments

An example of its use:


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))

Sample output

(-1, 5, 7)
'''
# Write your solution here
def create_tuple(x: int, y: int, z: int) -> tuple[int]:
    temp = [x, y, z]
    
    return (min(temp), max(temp), sum(temp))
    
if __name__ == '__main__':
    print('Exercício 1')
    t = create_tuple(25, 5, 0)
    print(t)    
    
'''
Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, and the second element is their year of birth. The function should find the oldest person on the list and return their name.

An example of the function in action:

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))

Sample output

Mary
'''
# Write your solution here
def oldest_person(people: list) -> str:
    oldestPerson = people[0]
    
    for person in people:
        if person[1] < oldestPerson[1]:
            oldestPerson = person
            
    return oldestPerson[0]

if __name__ == '__main__':
    print('Exercício 2')
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    p4 = ("Johnson", 1944)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))
    
'''
In this exercise we are handling tuples just like the ones described in the previous exercise.

Please write a function named older_people(people: list, year: int), which selects all those people on the list who were born before the year given as an argument. The function should return the names of these people in a new list.

An example of its use:

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

older = older_people(people, 1979)
print(older)

Sample output

[ 'Adam', 'Mary' ]
'''
# Write your solution here
def older_people(people: list, year: int) -> list[str]:
    return [person[0] for person in people if person[1] < year]

if __name__ == '__main__':
    print('Exercício 3')
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)

'''
NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

In this series of exercises you will create a simple student database. Before diving in, please spend a moment reading through the instructions and thinking about what sort of data structures are necessary for organising the data stored by your program.
adding students

First write a function named add_student, which adds a new student to the database. Also write a preliminary version of the function print_student, which prints out the information of a single student.

These function are used as follows:

students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")

Your program should now print out
Sample output

Peter:
 no completed courses
Eliza:
 no completed courses
Jack: no such person in the database

adding completed courses

Please write a function named add_course, which adds a completed course to the information of a specific student in the database. The course data is a tuple consisting of the name of the course and the grade:

students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
print_student(students, "Peter")

When some courses have been added, the information printed out changes:
Sample output

Peter:
 2 completed courses:
  Introduction to Programming 3
  Advanced Course in Programming 2
 average grade 2.5

repeating courses

Courses with grade 0 should be ignored when adding course information. Additionally, if the course is already in the database in that specific student's information, the grade recorded in the database should never be lowered if the course is repeated.

students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
print_student(students, "Peter")

Sample output

Peter:
 2 completed courses:
  Introduction to Programming 3
  Advanced Course in Programming 2
 average grade 2.5

summary of database

Please write a function named summary, which prints out a summary based on all the information stored in the database.

students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
add_course(students, "Peter", ("Data Structures and Algorithms", 1))
add_course(students, "Peter", ("Introduction to Programming", 1))
add_course(students, "Peter", ("Advanced Course in Programming", 1))
add_course(students, "Eliza", ("Introduction to Programming", 5))
add_course(students, "Eliza", ("Introduction to Computer Science", 4))
summary(students)

This should print out
Sample output

students 2
most courses completed 3 Peter
best average grade 4.5 Eliza
'''
# Write your solution here
def add_student(students : dict, name : str):
    students[name] = []

def print_student(students : dict, name : str):
    if name not in students:
        print(f'{name}: no such person in the database')
        return
    
    print(f"{name}:")
    
    if len(students[name]) == 0:
        print(' no completed courses')
    else:
        gradesSum = 0
        coursesLen = len(students[name])
        print(f' {coursesLen} completed courses:')
        for course in students[name]:
            print(f'  {course[0]} {course[1]}')
            gradesSum += course[1]

        print(f' average grade {gradesSum / coursesLen}')
        
def add_course(students : dict, name : str, course : tuple):
    if course[1] == 0:
        return
    
    alreadyIn = False
    
    for i in range(len(students[name])):
        if course[0] == students[name][i][0]:
            alreadyIn = True 
            if course[1] > students[name][i][1]:
                students[name][i] = course
            
    
    if alreadyIn == False:
        students[name].append(course)
        
def summary(students : dict):
    print(f'students {len(students)}')
    
    mostCoursesCompleted = ['', 0]
    
    for student in students:
        if len(students[student]) > mostCoursesCompleted[1]:
            mostCoursesCompleted[0] = student
            mostCoursesCompleted[1] = len(students[student])
                
    print(f'most courses completed {mostCoursesCompleted[1]} {mostCoursesCompleted[0]}')
    
    bestAvgGrade = ['', 0]
    
    for student in students:
        total = 0
        
        if len(students[student]) != 0:
            for courses in students[student]:
                total += courses[1]
            
            avg  = total / len(students[student])
        
        if avg > bestAvgGrade[1]:
            bestAvgGrade[0] = student
            bestAvgGrade[1] = avg

    print(f'best average grade {bestAvgGrade[1]} {bestAvgGrade[0]}')
            
if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
