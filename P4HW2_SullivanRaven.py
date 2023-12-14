#CTI-110
#P4HW2 - Salary Calculator
#Raven Sullivan
#11/15/2023

total_employees = 0
overtime_paid = 0.0
regular_paid = 0.0
total_gross = 0.0

while True:
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")
    if employee_name == 'Done':
       break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    print()
    
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay_rate = pay_rate * 1.5
    else:
        overtime_hours = 0
        overtime_pay_rate = 0

    overtime_pay = overtime_hours * overtime_pay_rate
    regular_pay = (hours_worked - overtime_hours) * pay_rate
    gross_pay = overtime_pay + regular_pay

    total_employees += 1
    overtime_paid += overtime_pay
    regular_paid += regular_pay
    total_gross += gross_pay

    print(f"Employee name:      {employee_name}\n")
    print("Hours Worked     Pay Rate    OverTime    OverTime Pay    RegHour Pay     Gross Pay")
    print("----------------------------------------------------------------------------------")
    print(f"{hours_worked:<16.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<16.2f}${regular_pay:<14.2f}${gross_pay:.2f}\n")

print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${overtime_paid:.2f}")
print(f"Total amount paid for regular hours: ${regular_paid:.2f}")
print(f"Total amount pain in gross: ${total_gross:.2f}")



    
