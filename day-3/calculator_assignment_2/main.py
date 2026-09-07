'''
2. Calculator Module 
Create: 
calculator/ 
├── main.py 
└── operations.py 
operations.py should contain: 
add() 
subtract() 
multiply() 
divide() 
main.py should: 
● Take user input 
● Perform the selected operation 
● Handle invalid numbers 
● Handle invalid operations 
● Handle division by zero 
'''


from operations_functional_approach import add, subtract, multiply, divide


def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number. Please enter numeric values.")
        return

    operation = input("Enter operation (+, -, *, /): ").strip()

    try:
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            return

        print("Result:", result)

    except ZeroDivisionError as e:
        print(e)


if __name__ == "__main__":
    main()
