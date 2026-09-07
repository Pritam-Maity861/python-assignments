'''
3. Number Analyzer 
Create functions: 
is_prime() 
is_even() 
is_odd() 
get_factors() 
get_prime_factors() 
Given a number: 
Enter number: 84 
Output: 
Even: Yes 
Prime: No 
Factors: [1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84] 
Prime Factors: [2, 3, 7] 
Handle 
● Negative numbers 
● Zero 
● One 
● Invalid input 
'''

'''
Functional Approach
'''
def is_prime(number):
    number = abs(number)

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def get_factors(number):
    number = abs(number)

    if number == 0:
        return []

    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors


def get_prime_factors(number):
    number = abs(number)

    if number <= 1:
        return []

    prime_factors = []

    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            prime_factors.append(i)

    return prime_factors


try:
    number = int(input("Enter number: "))

    if number == 0:
        print("Zero is neither prime nor odd/even.")
        print("Factors: []")
        print("Prime Factors: []")

    else:
        print("Even:", "Yes" if is_even(number) else "No")
        print("Odd:", "Yes" if is_odd(number) else "No")
        print("Prime:", "Yes" if is_prime(number) else "No")
        print("Factors:", get_factors(number))
        print("Prime Factors:", get_prime_factors(number))

except ValueError:
    print("Invalid input. Please enter a whole number.")

