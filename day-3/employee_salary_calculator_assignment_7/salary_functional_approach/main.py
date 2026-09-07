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
Functional Approach
'''

from calculations import (
    calculate_basic_salary,
    calculate_hra,
    calculate_da,
    calculate_bonus,
    calculate_tax,
    calculate_net_salary
)
from validators import (
    validate_salary,
    validate_experience
)

employee = {
    "name": "Ashmita",
    "basic_salary": 100000,
    "experience": 1
}

try:
    validate_salary(employee["basic_salary"])
    validate_experience(employee["experience"])
    basic_salary = calculate_basic_salary(
        employee["basic_salary"]
    )

    hra = calculate_hra(basic_salary)
    da = calculate_da(basic_salary)
    bonus = calculate_bonus(
        basic_salary,
        employee["experience"]
    )
    tax = calculate_tax(
        basic_salary,
        hra,
        da,
        bonus
    )
    net_salary = calculate_net_salary(
        basic_salary,
        hra,
        da,
        bonus,
        tax
    )

    print("Name:", employee["name"])
    print("Basic Salary:", basic_salary)
    print("HRA:", hra)
    print("DA:", da)
    print("Bonus:", bonus)
    print("Tax:", tax)
    print("Net Salary:", net_salary)

except ValueError as error:
    print("Error:", error)
