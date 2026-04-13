'''
Please write a program which asks the user for their date of birth, and then prints out how old the user was on the eve of the new millennium. The program should ask for the day, month and year separately, and print out the age in days. Please have a look at the examples below:
Sample output

Day: 10
Month: 9
Year: 1979
You were 7417 days old on the eve of the new millennium.
Sample output

Day: 28
Month: 3
Year: 2005
You weren't born yet on the eve of the new millennium.

You may assume all day-month-year combinations given as an argument will be valid dates. That is, there will not be a date like February 31st.
'''
# Write your solution here
from datetime import datetime, timedelta

NEWMILLENIUMSEVE = datetime(1999, 12, 31)

def getUserBithdate() -> datetime:
    birthDay = int(input('Day: '))
    birthMonth = int(input('Month: '))
    birthYear = int(input('Year: '))
    
    return datetime(birthYear, birthMonth, birthDay)

#ME =  New millenium's eve
def getNMEAge(userBirthdate : datetime) -> timedelta:
    return NEWMILLENIUMSEVE - userBirthdate    

def main():
    print('Exercício 1')
    userBirthdate = getUserBithdate()
    age = getNMEAge(userBirthdate)
    
    if age.days < 0:
        print("You weren't born yet on the eve of the new millennium.")
    else:
        print(f'You were {age.days} days old on the eve of the new millennium.')
        
main()

'''
In this exercise you will validate Finnish Personal Identity Codes (PIC).

Please write a function named is_it_valid(pic: str), which returns True or False based on whether the PIC given as an argument is valid or not. Finnish PICs follow the format ddmmyyXyyyz, where ddmmyy contains the date of birth, X is the marker for century, yyy is the personal identifier and z is a control character.

The program should check the validity by these three criteria:

    The first half of the code is a valid, existing date in the format ddmmyy.
    The century marker is either + (1800s), - (1900s) or A (2000s).
    The control character is valid.

The control character is calculated by taking the nine-digit number created by the date of birth and the personal identifier, dividing this by 31, and selecting the character at the index specified by the remainder from the string 0123456789ABCDEFHJKLMNPRSTUVWXY. For example, if the remainder was 12, the control character would be C.

More examples and explanations of the uses of the PIC are available at the Digital and Population Data Services Agency.

NB! Please make sure you do not share your own PIC, for example in the code you use for testing or through the course support channels.

Here are some valid PICs you can use for testing:

    230827-906F
    120488+246L
    310823A9877
'''
# Write your solution here
def isLeapYear(year : int) -> bool:
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False
    
    CENTURYMARKERS = ('+', '-', 'A')
    CCSTRING = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    
    dd = pic[0:2]
    mm = pic[2:4]
    yy = pic[4:6]
    centuryMarker = pic[6]
    personalIdentifier = pic[7:10]
    controlCharacter = pic[-1]
    
    if centuryMarker not in CENTURYMARKERS:
        return False
    
    if centuryMarker == 'A':
        temp = '20' + yy
        currentYear = datetime.now()
        
        if int(temp) > currentYear.year:
            return False
        
    if int(dd) > 31 or dd == '00':
        return False
    
    if int(mm) > 12 or mm == '00':
        return False
    
    if mm == '02':
        if centuryMarker == '+':
            temp = '18' + yy
        elif centuryMarker == '-':
            temp = '19' + yy
        else:
            temp = '20' + yy
        
        leapYear = isLeapYear(int(temp))
        
        if leapYear and int(dd) > 29:
            return False
        
        if not leapYear and int(dd) > 28:
            return False
    
    ccModuleCheck = dd + mm + yy + personalIdentifier
    ccModule = int(ccModuleCheck) % 31

    if CCSTRING[ccModule] != controlCharacter:
        return False
    
    return True
    
if __name__ == '__main__':
    print('Exercício 2')
    pic = '290200A1239'
    print(is_it_valid(pic))
    
'''
Please write a program for recording the amount of time the user has spent in front of a television, computer or mobile device screen over a specific period of time.

The program should work as follows:
Sample output

Filename: late_june.txt
Starting date: 24.6.2020
How many days: 5
Please type in screen time in minutes on each day (TV computer mobile):
Screen time 24.06.2020: 60 120 0
Screen time 25.06.2020: 0 0 0
Screen time 26.06.2020: 180 0 0
Screen time 27.06.2020: 25 240 15
Screen time 28.06.2020: 45 90 5
Data stored in file late_june.txt

The user will input each day on a separate line, and the entries will contain three numbers separated by spaces, representing minutes.

With the above input, the program should store the data in a file named late_june.txt. The contents should look like this:
Sample data

Time period: 24.06.2020-28.06.2020
Total minutes: 780
Average minutes: 156.0
24.06.2020: 60/120/0
25.06.2020: 0/0/0
26.06.2020: 180/0/0
27.06.2020: 25/240/15
28.06.2020: 45/90/5
'''
print('Exercício 3')
filename = input('Filename: ')
inputDate = input('Starting date: ')
startDate = datetime.strptime(inputDate, "%d.%m.%Y")
endDate = startDate
quantityDays = int(input('How many days: '))
days = []

print('Please type in screen time in minutes on each day (TV computer mobile):')

for i in range(quantityDays):
    if(i != 0):
        endDate = endDate + timedelta(days=1)

    temp = input(endDate.strftime("Screen time %d.%m.%Y: "))
    minutes = temp.split(' ')
    intMinutes = [int(num) for num in minutes]
    days.append(intMinutes)
    
print(f'Data stored in file {filename}')

timePeriod = 'Time period: ' + startDate.strftime("%d.%m.%Y") + '-' + endDate.strftime("%d.%m.%Y")
totalMinutesDay = [sum(day) for day in days]
avgMinutes = sum(totalMinutesDay) /  quantityDays

tempDate = startDate
formattedMinutesDay = []

for i in range(quantityDays):
    day = tempDate.strftime("%d.%m.%Y:")
    temp = f'{day} {days[i][0]}/{days[i][1]}/{days[i][2]}'
    formattedMinutesDay.append(temp)
    tempDate = tempDate + timedelta(days=1)

fileText = f'{timePeriod}\nTotal minutes: {sum(totalMinutesDay)}\nAverage minutes: {avgMinutes}\n'

for i in range(quantityDays):
    if i == quantityDays - 1:
        fileText += formattedMinutesDay[i]
    else:
        fileText += formattedMinutesDay[i] + '\n'
    
with open(filename, 'w') as myFile:
    myFile.write(fileText);
