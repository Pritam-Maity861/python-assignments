def validate_salary(basic_salary):
    if basic_salary <= 0:
        raise ValueError("Salary must be greater than 0.")


def validate_experience(experience):
    if experience < 0:
        raise ValueError("Experience cannot be negative.")
