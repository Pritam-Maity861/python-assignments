def calculate_basic_salary(basic_salary):
    return basic_salary

def calculate_hra(basic_salary):
    return basic_salary * 0.20

def calculate_da(basic_salary):
    return basic_salary * 0.10

def calculate_bonus(basic_salary, experience):
    if experience >= 2:
        return basic_salary * 0.05

    return 0

def calculate_tax(basic_salary, hra, da, bonus):
    gross_salary = basic_salary + hra + da + bonus

    return gross_salary * 0.10

def calculate_net_salary(basic_salary, hra, da, bonus, tax):
    gross_salary = basic_salary + hra + da + bonus

    return gross_salary - tax
