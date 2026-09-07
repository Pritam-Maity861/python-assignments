class SalaryCalculator:
    def calculate_basic_salary(self, basic_salary):
        return basic_salary

    def calculate_hra(self, basic_salary):
        return basic_salary * 0.20

    def calculate_da(self, basic_salary):
        return basic_salary * 0.10

    def calculate_bonus(self, basic_salary, experience):
        if experience>=2:
            return basic_salary * 0.05

        return 0

    def calculate_tax(self, basic_salary, hra, da, bonus):
        gross_salary= basic_salary + hra + da + bonus

        return gross_salary * 0.10

    def calculate_net_salary(self,basic_salary,hra,da,bonus,tax):
        gross_salary=basic_salary + hra + da + bonus

        return gross_salary - tax
