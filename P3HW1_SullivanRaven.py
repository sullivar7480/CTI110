#P3HW1
#10/19/2023
#CTI-110
#Raven Sullivan
#This program takes a number grade, determines average, and displays letter grade for average


mod_1 = float(input("Enter number grade for Module 1: "))
mod_2 = float(input("Enter number grade for Module 2: "))
mod_3 = float(input("Enter number grade for Module 3: "))
mod_4 = float(input("Enter number grade for Module 4: "))
mod_5 = float(input("Enter number grade for Module 5: "))
mod_6 = float(input("Enter number grade for Module 6: "))

#Add Grades entered to a list

grades = [mod_1,mod_2,mod_3,mod_4,mod_5,mod_6]

#Determine lowest, highest, sum and average for grades.

low = min(grades)
high = max(grades)
sum_of_grades = sum(grades)
avg = sum_of_grades/6

#Display Results

print("\n-----------Results-----------")

print(f'{"Lowest Grade:":<20}{low}')
print(f'{"Highest Grade:":<20}{high}')
print(f'{"Sum of Grades:":<20}{sum_of_grades}')
print(f'{"Average:":<20}{avg:.2f}')

print("\n-----------Results-----------")

#Determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')

    
