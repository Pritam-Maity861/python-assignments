'''
Assignment 2: Comprehensions: list, dictionary 
'''

squares = [x**2 for x in range(10)]
print(squares)


labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)



squares_dict = {x: x**2 for x in range(5)}

print(squares_dict)



original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}

print(swapped)



names = ["Tarun", "Alinda", "Pritam"]
ages = [25, 30, 22]
people = {name: age for name, age in zip(names, ages)}

print(people)