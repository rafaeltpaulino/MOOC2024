#Criei esse arquivo separado, pois é um exercício muito grande
# tee ratkaisu tänne
def readCSVFile(fileName : str) -> list:
    res = []
    
    with open (fileName) as newFile:
        for line in newFile:
            line = line.strip()
            data = line.split(';')
            if data[0] != 'id':
                res.append(data)
            
    return res

def readTXTFile(filename : str) -> list:
    res = []
    
    with open(filename) as file:
        for line in file:
            res.append(line.rstrip())        

    return res

def createStudentDict(studentData : list) -> dict:
    students = {}
    
    for student in studentData:
        students[student[0]] = f'{student[1]} {student[2]}'
        
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

def generateResultsFile(filename : str, results : list, courseInfo : str):
    with open(filename, 'w') as newFile:
        if '.txt' in filename:
            newFile.write(f'{courseInfo}\n')
            newFile.write(f'{'=' * 38}\n')
            newFile.write(f'name{' ' * 26}exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n')
            
        for result in results:
            result += '\n'
            newFile.write(result)
            
    
def courseGrading():
    studentFile = input('Student information: ')
    exercisesFile = input('Exercises completed: ')
    examsFile = input('Exam points: ')
    courseFile =  input('Course information: ')
    
    students = createStudentDict(readCSVFile(studentFile))
    exercises = createExercisesDict(readCSVFile(exercisesFile))
    exams = createExercisesDict(readCSVFile(examsFile))
    course = readTXTFile(courseFile)
    temp1 = course[0].replace('name: ', '')
    temp2 = course[1].replace('study credits: ', '')
    courseInfo = f'{temp1}, {temp2} credits'
    
    resultsTxt = []
    resultsCsv = []
        
    print(f'name{' ' * 26}exec_nbr  exec_pts. exm_pts.  tot_pts.  grade')
    
    for studentID in students:
        studentName = students[studentID]
        totalExercisesCompleted = sum(exercises[studentID])
        exercisePoints = calculateExercisePoints(exercises[studentID])
        examPoints = calculateExamPoints(exams[studentID])
        totalPoints = exercisePoints + examPoints
        grade = getGrade(exercisePoints, examPoints)
        
        txt = f'{studentName:30}{totalExercisesCompleted:<10}{exercisePoints:<10}{examPoints:<10}{totalPoints:<10}{grade:<10}'
        csv = f'{studentID};{studentName};{grade}'
        resultsTxt.append(txt)
        resultsCsv.append(csv)
        print(txt)
    
    generateResultsFile('results.txt', resultsTxt, courseInfo)    
    generateResultsFile('results.csv', resultsCsv, courseInfo)
    print('Results written to files results.txt and results.csv')
    

def main():        
    print('Exercício 5')   
    courseGrading()
        
main()
