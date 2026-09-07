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
class base approach
'''
class NumberAnalyzer:

    def __init__(self, number):
        self.number = number

    def is_prime(self):
        if self.number <= 1:
            return False

        for i in range(2, self.number):
            if self.number % i == 0:
                return False

        return True

    def is_even(self):
        return self.number % 2 == 0

    def is_odd(self):
        return self.number % 2 != 0

    def get_factors(self):
        if self.number == 0:
            return []

        factors = []

        for i in range(1, abs(self.number) + 1):
            if self.number % i == 0:
                factors.append(i)

        return factors

    def get_prime_factors(self):
        number = abs(self.number)
        prime_factors = []

        if number < 2:
            return prime_factors

        for i in range(2, number + 1):
            if number % i == 0:
                if NumberAnalyzer(i).is_prime():
                    prime_factors.append(i)

        return prime_factors



try:
    number = int(input("Enter number: "))

    analyzer = NumberAnalyzer(number)

    if number == 0:
        print("Zero is neither prime nor odd/even.")
        print("Factors: []")
        print("Prime Factors: []")

    else:
        print("Even:", "Yes" if analyzer.is_even() else "No")
        print("Odd:", "Yes" if analyzer.is_odd() else "No")
        print("Prime:", "Yes" if analyzer.is_prime() else "No")
        print("Factors:", analyzer.get_factors())
        print("Prime Factors:", analyzer.get_prime_factors())

except ValueError:
    print("Invalid input. Please enter a valid number.")