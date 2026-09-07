class SalaryValidator:
    def validate_salary(self, basic_salary):
        if basic_salary<=0:
            raise ValueError("Salary must be greater than 0.")

    def validate_experience(self, experience):
        if experience<0:
            raise ValueError("Experience cannot be negative.")
