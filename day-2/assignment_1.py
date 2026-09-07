'''
Assigment 1: Explore all the methods of collections framework and write down coding example 
'''

'''
List collections
'''
list1=[1,2,3,4,5]
# Adds an item at the end
list1.append(6)
print(list1)

list2=[7,8,9]
# list1.append(list2)
# print(list1)

# Adds multiple items
list1.extend(list2)
print(list1)

# Adds an item at a specific index position
list1.insert(1,10)
print(list1)

# for removing a specific value
list1.remove(10) 
print(list1)

# pop() remove the element base on index and also return the value
returnValue=list1.pop(2)
print(returnValue) 
print(list1)

#for finding the position of an element we have index() method.
indexValue=list1.index(1)
print(indexValue)  #0

list3=[10,20,30,20,40,10,50,10]
print(list3.count(10))  #3     count() it's use to count the occurence of any value in the list
print(list3.count(20))  #2

list3.sort()   #this method sort the list in place and we can also can also sort it in ascending and descending order
print("ascending ->", list3)
list3.sort(reverse=True)
print("descending ->", list3)

#for reverse the list reverse()
list4=[1,5,7,9,10]
list4.reverse()  #in place
print(list4)

# for copy list
list4_copy=list4.copy()
list4_copy.remove(5)
print("original list --> ", list4)
print("copy list -->", list4_copy)

#for clear the entire list we have clear()
list4.clear()
print(list4)   #[]

'''
Tuple collections
'''
t1=("A","B","C","D","E","A","F","A")
#for counting the occurence of a specific value
print(t1.count("A"))  #3

# for finding the position of an element
print(t1.index("D"))  #3

# index base access
print(t1[0])  #A


'''
Set collections
'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.add(7)
print(a) # {1, 2, 3, 4, 7}

a.update([8, 9])
print(a) # {1, 2, 3, 4, 7, 8, 9}

a.remove(9)
print(a)  # {1, 2, 3, 4, 7, 8}

a.discard(10)   # No error even 10 is absent

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

result = A.union(B)
print(result)   # {1, 2, 3, 4, 5, 6, 7, 8}

# #using or operator
# result = A | B
# print(result) # {1, 2, 3, 4, 5, 6, 7, 8}

result = A.intersection(B)
print(result)   # {4, 5}

# # using & operator
# result = A & B
# print(result)   # {4, 5}

result = A.difference(B)
print(result)   # {1, 2, 3}

# # Using - operator
# result = A - B
# print(result)   # {1, 2, 3}


result = A.symmetric_difference(B)
print(result)       # {1, 2, 3, 6, 7, 8}


C = {1, 2, 3, 4, 5}
D = {1, 2, 3}

print(D.issubset(C))    # True
print(C.issuperset(D))  # True

set_A = {1, 2, 3}
set_B = {4, 5, 6}

print(set_A.isdisjoint(set_B))  # True

a.clear()
print(a)    # set()


'''
Dictionary collections
'''
student = {
    "name": "Pritam",
    "age": 21,
    "course": "Backend"
}

print(student.get("name"))  # Pritam

print(student.keys())      # dict_keys(['name', 'age', 'course'])

print(student.values())  # dict_values(['Pritam', 21, 'Backend'])

print(student.items())     # dict_items([('name', 'Pritam'), ('age', 21), ('course', 'Backend')])

student.update({"age": 22, "city": "Kolkata"})
print(student)  # {'name': 'Pritam', 'age': 22, 'course': 'Backend', 'city': 'Kolkata'}

student.pop("city")
print(student)      # {'name': 'Pritam', 'age': 22, 'course': 'Backend'}

# Gets a value or creates the key
student.setdefault("email", "pritam@company.com")
print(student)      #{'name': 'Pritam', 'age': 22, 'course': 'Backend', 'email': 'pritam@company.com'}

# Removes the last key-value pair
student.popitem()    
print(student)      #{'name': 'Pritam', 'age': 22, 'course': 'Backend'}

student.clear()
print(student)  # {}


'''
Frozenset collections
'''
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])

print(a.union(b))   # frozenset({1, 2, 3, 4, 5, 6})

print(a.intersection(b))    # frozenset({3, 4})

print(a.difference(b))  # frozenset({1, 2})

c = frozenset([1, 2])

print(c.issubset(a))    # True

print(a.issuperset(c))  # True

print(a.isdisjoint(frozenset([10, 20])))    # True
