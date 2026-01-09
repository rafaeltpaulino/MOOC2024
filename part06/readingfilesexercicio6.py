#Criei esse arquivo pelo mesmo motivo que criei o outro, exercício bem grande e geraria conflito caso colocasse esse código no arquivo readingfiles.py
# tee ratkaisu tänne
# wwite your solution here
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

def createExercisesDict(exercisesData : list) -> dict:
    exercises = {}
    
    for entry in exercisesData:
        exercises[entry[0]] = [int(point) for point in entry[1:]]
        
    return exercises

def createExamDict(examsData : list) -> dict:
    exams = {}
    
    for entry in examsData:
        exams[entry[0]] = [int(point) for point in entry[1:]]
    
    return exams

def calculateExercisePoints(exercisesCompleted : list) -> int:
    return sum(exercisesCompleted) // 4

def calculateExamPoints(examPoints : list) -> int:
    return sum(examPoints)

def getGrade(exercisePoints : int, examPoints : int) -> int:
    grade = 0
    pointsSum = exercisePoints + examPoints
    
    if pointsSum < 15:
        grade = 0
    elif pointsSum < 18:
        grade = 1 
    elif pointsSum < 21:
        grade = 2
    elif pointsSum < 24:
        grade = 3
    elif pointsSum < 28:
        grade = 4
    else:
        grade = 5
    
    return grade
    
    
def courseGrading():
    studentFile = input('Student information: ')
    exercisesFile = input('Exercises completed: ')
    examsFile = input('Exam points: ') 
    
    students = createStudentDict(readFile(studentFile))
    exercises = createExercisesDict(readFile(exercisesFile))
    exams = createExercisesDict(readFile(examsFile))
        
    print(f'name{' ' * 26}exec_nbr  exec_pts. exm_pts.  tot_pts.  grade')
    
    for studentID in students:
        studentName = students[studentID][0] + ' ' + students[studentID][1]
        totalExercisesCompleted = sum(exercises[studentID])
        exercisePoints = calculateExercisePoints(exercises[studentID])
        examPoints = calculateExamPoints(exams[studentID])
        totalPoints = exercisePoints + examPoints
        grade = getGrade(exercisePoints, examPoints)
        
        print(f'{studentName:30}{totalExercisesCompleted:<10}{exercisePoints:<10}{examPoints:<10}{totalPoints:<10}{grade:<10}')

def main():           
    courseGrading()
    
main()
