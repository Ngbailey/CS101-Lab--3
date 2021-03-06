########################################################################
##
## CS 101 Lab
## Program # 2 week 3
## Name: Nathan Bailey
## Email: ngbailey@ucsd.edu
##
## PROBLEM : Calculating Grades
##
## ALGORITHM :
print('##### WELCOME TO THE LAB GRADE CALCULATOR #####\n')
user = input('Whose grade are we calculating for today?\n')
userLabs = float(input('Please enter your Labs grade between 0-100\n'))
userExams = float(input('Please enter your Lab Exams grade between 0-100\n'))
userAttendance = float(input('Please enter your Attendance grade between 0-100\n'))
if 0 > userLabs:
    userLabs = 0
    print('WARNING!!, do not input values below 0, your Labs score has been set to 0.\n')

    
if 100 < userLabs:
    userLabs = 100
    print('WARNING!!, do not input values above 100, your Labs score has been set to 100.\n')

    
if 0 > userExams:
    userExams = 0
    print('WARNING!!, do not input values below 0, your Lab Exams score has been set to 0.\n')

    
if 100 < userExams:
    userExams = 100
    print('WARNING!!, do not input values above 100, your Lab Exams score has been set to 100.\n')

    
if 0 > userAttendance:
    userAttendance = 0
    print('WARNING!!, do not input values below 0, your Attendance score has been set to 0.\n')

if 100 < userAttendance:
    userAttendance = 100
    print('WARNING!!, do not input values above 100, your Attendance score has been set to 100.\n')

labsGrade = userLabs * 0.7
examsGrade = userExams * 0.2
attendance = userAttendance * 0.1
grade = 'uknown'
weightedGrade = labsGrade + examsGrade + attendance
weightedGrade = round(weightedGrade, 2)
if 90<= weightedGrade <= 100:
    grade = 'A'
elif 80 <= weightedGrade < 90:
    grade = 'B'
elif 70 <= weightedGrade < 80:
    grade = 'C'
elif 60 <= weightedGrade < 70:
    grade = 'D'
elif 0 <= weightedGrade < 60:
    grade = 'F'
else:
    grade = 'ERROR, something went wrong'

print('The weighted Grade for {1} is {0}\n'.format(weightedGrade, user,))
print('{} has a letter grade of {}.\n'.format(user, grade,))
print('##### THANK YOU FOR USING THE LAB GRADE CALCULATOR!!! #####')
##          
## 
## ERROR HANDLING:
##      If users enter a value outside of the range of 0-100 they
##      will be warned and their incorrect inputs will be corrected.
##
## OTHER COMMENTS:
##      
##
########################################################################
