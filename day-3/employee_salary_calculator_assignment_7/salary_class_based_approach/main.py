'''
7. Employee Salary Calculator 
Input: 
employee = { 
"name": "Ashmita", 
"basic_salary": 100000, 
"experience": 1 
} 
Calculate: 
Basic Salary 
HRA 
DA 
Bonus 
Tax 
Net Salary 
Create separate functions for each calculation. 
Structure 
salary/ 
├── main.py 
├── calculations.py 
└── validators.py 
Invalid salary or experience should raise appropriate exceptions.
'''

'''
class base Approach
'''

from calculations import SalaryCalculator
from validators import SalaryValidator

employee = {
    "name": "Ashmita",
    "basic_salary": 100000,
    "experience": 1
}

calculator = SalaryCalculator()
validator = SalaryValidator()


try:
    validator.validate_salary(employee["basic_salary"])

    validator.validate_experience(employee["experience"])

    basic_salary = calculator.calculate_basic_salary(employee["basic_salary"])

    hra = calculator.calculate_hra(basic_salary)

    da = calculator.calculate_da(basic_salary)

    bonus = calculator.calculate_bonus(basic_salary, employee["experience"])

    tax = calculator.calculate_tax(basic_salary,hra,da,bonus)

    net_salary = calculator.calculate_net_salary(basic_salary,hra,da,bonus,tax)

    print("Name:", employee["name"])
    print("Basic Salary:", basic_salary)
    print("HRA:", hra)
    print("DA:", da)
    print("Bonus:", bonus)
    print("Tax:", tax)
    print("Net Salary:", net_salary)

except ValueError as error:
    print("Error:", error)
