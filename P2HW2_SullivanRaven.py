#CTI-110
#P2HW2 - List
#Raven Sullivan
#9/19/2023
#


module_1 = float(input('Enter Grade for Module 1: '))
module_2 = float(input('Enter Grade for Module 2: '))
module_3 = float(input('Enter Grade for Module 3: '))
module_4 = float(input('Enter Grade for Module 4: '))
module_5 = float(input('Enter Grade for Module 5: '))
module_6 = float(input('Enter Grade for Module 6: '))

print('\n-----------Results-----------')

grades = [module_1 , module_2 , module_3 , module_4 , module_5 , module_6]

lowest_grades = min(grades)
highest_grades = max(grades)
sum_grades = sum(grades)
avg_grades = sum(grades)/len(grades)

print(f' Lowest Grade: {lowest_grades}')
print(f' Highest Grade: {highest_grades}')
print(f' Sum of Grades: {sum_grades}')
print(f' Average: {avg_grades:.2f}')

