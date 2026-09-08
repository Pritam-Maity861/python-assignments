"""
Assignment 4: Standard Class vs Python Dataclass
"""

from dataclasses import dataclass

class StandardUser:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"I am {self.name} object, with {self.salary} salary"

    def __str__(self):
        return f"User(Name: {self.name}, Age: {self.age}, Salary: ${self.salary})"

    def __eq__(self, other):
        if not isinstance(other, StandardUser):
            return False
        return (self.name, self.age, self.salary) == (other.name, other.age, other.salary)


@dataclass
class User:
    name: str
    age: int
    salary: float


if __name__ == "__main__":
    u1_manual = StandardUser("Pritam", 24, 50000.0)
    u2_manual = StandardUser("Pritam", 24, 50000.0)

    print("Standard Manual Class")
    print(f"__repr__: {repr(u1_manual)}")
    print(f"__str__: {u1_manual}")
    print(f"Equality Check (u1 == u2): {u1_manual == u2_manual}")

    print("\n Python @dataclass ")
    u1_data = User("Pritam", 24, 50000.0)
    u2_data = User("Pritam", 24, 50000.0)

    print(f"Auto-generated __repr__: {u1_data}")
    print(f"Auto-generated Equality Check (u1 == u2): {u1_data == u2_data}")
