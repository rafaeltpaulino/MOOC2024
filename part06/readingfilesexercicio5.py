# wwite your solution here
#Criei um arquivo próprio para esse exercício, pois ele é uma melhoria do exercício 4, portanto daria conflitos caso eu simplesmente colocasse 
# esse código no arquivo readingfiles.py. Outro motivo é o tamanho do exercício, acho que fica melhor em seu próprio arquivo por ser muito grande.
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
    
def calculateGrades(students : dict, exercises : dict, exams : dict) -> dict:
    grades = {}
    
    for studentID in students:
        if studentID in exercises and exams:
            studentName = students[studentID][0] + ' ' + students[studentID][1]
            exercisePoints = calculateExercisePoints(exercises[studentID])
            examPoints = calculateExamPoints(exams[studentID])
            grades[studentName] = getGrade(exercisePoints, examPoints)
            
    return grades
    
def courseGrading(): 
    studentFile = input('Student information: ')
    exercisesFile = input('Exercises completed: ')
    examsFile = input('Exam points: ')
    
    students = createStudentDict(readFile(studentFile))
    exercises = createExercisesDict(readFile(exercisesFile))
    exams = createExercisesDict(readFile(examsFile))
    
    grades = calculateGrades(students, exercises, exams)
    
    for student, grade in grades.items():
        print(f'{student} {grade}')

def main():           
    courseGrading()
    
main()
