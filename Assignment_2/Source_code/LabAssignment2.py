'''
CS 101 Lab
Program 2
Jacob Ford
jwfhmp@umkc.edu
'''

print('*'*4,'Welcome to the LAB grade calculator!','*'*4)
student_name = input('\nWho are we calculating grades for? ==> ')
labs_grade = int(input('\nEnter the Labs grade? ==> '))
if labs_grade > 100:
    labs_grade = 100
    print('The lab value should have been 100 or less. It has been changed to 100.')
elif labs_grade < 0:
    labs_grade = 0
    print('The lab value should have been zero or greater. It has been changed to zero.')
exams_grade = int(input('\nEnter the EXAMS grade? ==> '))
if exams_grade > 100:
    exams_grade = 100
    print('The exam value should have been 100 or less. It has been changed to 100.')
elif exams_grade < 0:
    exams_grade = 0
    print('The exam value should have been zero or greater. It has been changed to zero.')
attendance_grade = int(input('\nEnter the Attendance grade? ==> '))
if attendance_grade > 100:
    attendance_grade = 100
    print('The attendance value should have been 100 or less. It has been changed to 100.')
elif attendance_grade < 0:
    attendance_grade = 0
    print('The attendance value should have been zero or greater. It has been changed to zero.')
weighted_grade = (exams_grade * .2) + (labs_grade * .7) + (attendance_grade * .1)
if weighted_grade >= 90:
    letter_grade = 'A'
elif weighted_grade >= 80:
    letter_grade = 'B'
elif weighted_grade >= 70:
    letter_grade = 'C'
elif weighted_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print('\nThe weighted grade for {} is {}'.format(student_name,weighted_grade))
print('{} has a letter grade of {}'.format(student_name,letter_grade))

