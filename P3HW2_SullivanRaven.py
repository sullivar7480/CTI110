#CTI-110
#P3HW2 - Salary
#Raven Sullivan
#10/19/2023
#This program calculates employee pay for hours worked with overtime

employee = input("Enter employee's name: ")

#ask for hours worked

hours_worked_week = float(input("Enter number of hours worked this week: "))

#ask user to enter employee's pay rate

pay_rate = float(input("Enter number of hours worked this week: "))

#Overtime

if hours_worked_week > 40:
    overtime = (hours_worked_week - 40)
else:
        overtime = 0

if hours_worked_week > 40:
    overtime_pay = overtime * (pay_rate * 1.5)
else:
        overtime_pay = 0

#Amount of pay for regular hours worked

if hours_worked_week < 0:
    reg_hours_pay = hours_worked_week * pay_rate
elif hours_worked_week <= 40:
    reg_hours_pay = hours_worked_week * pay_rate
else:
    reg_hours_pay = 40 * pay_rate

#Gross Pay

gross_pay = reg_hours_pay + overtime_pay

#Display Output

print('----------------------------------------------')
print("Hours Work\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
print('------------------------------------------------------------------------------------------')
print(f'{hours_worked_week:.1f}\t\t${pay_rate:.2f}\t\t{overtime:.1f}\t\t${overtime_pay:.2f}\t\t${reg_hours_pay:.2f}\t\t${gross_pay:.2f}')
      
